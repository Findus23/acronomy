from urllib.parse import unquote

from django.db import models
from simple_history.models import HistoricalRecords

from acros.models import Acronym, WikipediaImage
from acros.utils.apis import WikipediaAPISummary


class WikipediaLink(models.Model):
    acronym = models.ForeignKey(Acronym, on_delete=models.CASCADE, related_name="wiki_articles")
    title = models.CharField(max_length=200)
    extract = models.TextField(blank=True)
    extract_html = models.TextField(blank=True)
    thumbnail = models.ForeignKey(WikipediaImage, on_delete=models.CASCADE, related_name="wiki_articles",
                                  blank=True, null=True)
    timestamp = models.DateTimeField(blank=True)
    fetched = models.BooleanField(default=False)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.fetched:
            summary = WikipediaAPISummary(self.title)
            self.extract = summary.extract
            self.extract_html = summary.extract_html
            self.timestamp = summary.timestamp
            self.title = summary.title
            if summary.image:
                filename = unquote(summary.image.split("/")[-1])
                try:
                    thumbnail = WikipediaImage.objects.get(filename=filename)
                except WikipediaImage.DoesNotExist:
                    thumbnail = WikipediaImage.objects.create(filename=filename)
                thumbnail.save()
                self.thumbnail = thumbnail
            self.fetched = True

        super(WikipediaLink, self).save(*args, **kwargs)

    @property
    def url(self):
        return f"https://en.wikipedia.org/wiki/{self.title}"

    def __str__(self):
        return self.title
