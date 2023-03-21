from urllib.parse import unquote

from django.core.exceptions import ValidationError
from django.db import models
from simple_history.models import HistoricalRecords

from acros.models import Acronym, WikipediaImage
from acros.utils.apis import WikipediaAPISummary, NotFoundError


class WikipediaLink(models.Model):
    acronym = models.ForeignKey(Acronym, on_delete=models.CASCADE, related_name="wiki_articles")
    title = models.CharField(max_length=200)
    extract = models.TextField(blank=True)
    extract_html = models.TextField(blank=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ForeignKey(WikipediaImage, on_delete=models.CASCADE, related_name="wiki_articles",
                                  blank=True, null=True)
    timestamp = models.DateTimeField(blank=True)
    fetched = models.BooleanField(default=False)
    history = HistoricalRecords()

    def clean(self):
        if not self.fetched:
            try:
                summary = WikipediaAPISummary(self.title)
            except NotFoundError as e:
                raise ValidationError(str(e))
            self.extract = summary.extract
            self.extract_html = summary.extract_html
            self.description = summary.description
            self.timestamp = summary.timestamp
            self.title = summary.title
            if summary.image:
                filename = unquote(summary.image.split("/")[-1])
                if filename.endswith(".svg.png"):
                    filename = summary.image.split("/")[-2]
                try:
                    thumbnail = WikipediaImage.objects.get(filename=filename)
                except WikipediaImage.DoesNotExist:
                    thumbnail = WikipediaImage.objects.create(filename=filename)
                success = thumbnail.save()
                if success:
                    self.thumbnail = thumbnail
            self.fetched = True

    @property
    def url(self):
        return f"https://en.wikipedia.org/wiki/{self.title.replace(' ', '_')}"

    def __str__(self):
        return self.title
