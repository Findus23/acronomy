from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from simple_history.models import HistoricalRecords

from acros.models import Tag
from acros.utils.conversion import md_to_html


def valid_acronym(value: str):
    if ":" in value:
        raise ValidationError('Acronyms are not allowed to contain a ":"')


class Acronym(models.Model):
    name = models.CharField(max_length=100, validators=[valid_acronym])
    full_name = models.CharField(max_length=1000)
    slug = models.SlugField(null=False, unique=True)
    acro_letters = ArrayField(
        models.SmallIntegerField(),
        null=True, blank=True
    )
    description_md = models.TextField(blank=True)
    description_html = models.TextField(editable=False)
    history = HistoricalRecords(excluded_fields=["created_date"])
    tags = models.ManyToManyField(Tag, related_name="acronyms")
    stub = models.BooleanField(default=True, help_text="check if this is a minimal entry that should be extended")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    pageviews = models.IntegerField(default=0, editable=False)

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.name)

        if not self.id:
            try:
                found = Acronym.objects.get(slug=self.slug)
            except Acronym.DoesNotExist:
                found = False
            if found:
                raise ValidationError(f"slug '{self.slug}' already exists")

        self.description_html = md_to_html(self.description_md)
        if not self.acro_letters:
            self.acro_letters = [0]
            for pos, char in enumerate(self.full_name):
                if char == " " and pos <= len(self.full_name):
                    self.acro_letters.append(pos + 1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

    def first_letter(self):
        return self.name and self.name[0] or ''

    class Meta:
        ordering = ["name"]


