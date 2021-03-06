from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from simple_history.models import HistoricalRecords


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, editable=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tag', args=[str(self.slug)])
