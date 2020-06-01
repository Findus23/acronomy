from urllib.parse import urlparse

from django.db import models
from simple_history.models import HistoricalRecords

from acros.models import Acronym, Host


class Weblink(models.Model):
    acronym = models.ForeignKey(Acronym, on_delete=models.CASCADE, related_name="links")
    url = models.URLField()
    host = models.ForeignKey(Host, on_delete=models.CASCADE, editable=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.url



    def save(self, *args, **kwargs):
        uri = urlparse(self.url)
        self.host, created = Host.objects.get_or_create(host=uri.hostname)
        super(Weblink, self).save(*args, **kwargs)
