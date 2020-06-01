from tempfile import TemporaryFile

import requests
from django.core.files import File
from django.db import models
from simple_history.models import HistoricalRecords

from acros.models import Acronym
from acros.utils import fetch_wikipedia_summary


class WikipediaLink(models.Model):
    acronym = models.ForeignKey(Acronym, on_delete=models.CASCADE, related_name="wiki_articles")
    title = models.CharField(max_length=200)
    extract = models.TextField(blank=True)
    extract_html = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="wikipedia_thumbnails/", blank=True,
                                  height_field="thumbnail_height", width_field="thumbnail_width")
    thumbnail_width = models.IntegerField(blank=True, editable=False)
    thumbnail_height = models.IntegerField(blank=True, editable=False)
    timestamp = models.DateTimeField(blank=True)
    fetched = models.BooleanField(default=False)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.fetched:
            self.extract, self.extract_html, self.timestamp, thumbnail = fetch_wikipedia_summary(self.title)
            with TemporaryFile("rb+") as fd:
                r = requests.get(thumbnail["source"])
                filename = thumbnail["source"].split("/")[-1]
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
                image_file = File(fd)
                self.thumbnail.save(filename, image_file, save=False)
            self.fetched = True

        super(WikipediaLink, self).save(*args, **kwargs)

    @property
    def url(self):
        return f"https://en.wikipedia.org/wiki/{self.title}"

    def __str__(self):
        return self.title
