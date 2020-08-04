from django.db import models

from acros.models import Acronym


class AcroOfTheDay(models.Model):
    acronym = models.ForeignKey(Acronym, on_delete=models.CASCADE)
    date = models.DateField()
    order = models.SmallIntegerField()

    class Meta:
        ordering = ["date", "order"]
