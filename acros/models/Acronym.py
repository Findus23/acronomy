from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from simple_history.models import HistoricalRecords

from acros.models import Tag
from acros.utils.conversion import md_to_html


class Acronym(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=1000)
    slug = models.SlugField(null=False, unique=True)
    description_md = models.TextField(blank=True)
    description_html = models.TextField(editable=False)
    history = HistoricalRecords()
    tags = models.ManyToManyField(Tag, related_name="acronyms")

    def save(self, *args, **kwargs):
        self.description_html = md_to_html(self.description_md)
        if not self.slug:
            self.slug = slugify(self.name)
        super(Acronym, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

    class Meta:
        ordering = ["name"]
