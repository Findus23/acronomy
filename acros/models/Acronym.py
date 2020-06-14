from django.core.exceptions import ValidationError
from django.db import models
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
    description_md = models.TextField(blank=True)
    description_html = models.TextField(editable=False)
    history = HistoricalRecords(excluded_fields=["created_date"])
    tags = models.ManyToManyField(Tag, related_name="acronyms")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.description_html = md_to_html(self.description_md)
        if not self.slug:
            self.slug = slugify(self.name)
        super(Acronym, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

    def first_letter(self):
        return self.name and self.name[0] or ''

    class Meta:
        ordering = ["name"]

    def clean(self):
        if not self.id:
            new_slug = slugify(self.name)
            try:
                found = Acronym.objects.get(slug=new_slug)
            except Acronym.DoesNotExist:
                found = False
            if found:
                raise ValidationError(f"slug '{new_slug}' already exists")
