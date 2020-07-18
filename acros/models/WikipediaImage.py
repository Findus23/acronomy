from tempfile import TemporaryFile

import requests
from django.core.files import File
from django.db import models

from acros.utils.apis import WikipediaImageAPIObject


class WikipediaImage(models.Model):
    filename = models.CharField(max_length=200)
    pageid = models.IntegerField()
    thumbnail = models.ImageField(upload_to="wikipedia_images/", blank=True, null=True)
    thumb_width = models.IntegerField(blank=True, editable=False, null=True)
    thumb_height = models.IntegerField(blank=True, editable=False, null=True)
    imageurl = models.URLField()
    caption = models.CharField(max_length=1000, null=True, blank=True)
    credit = models.TextField()
    artist = models.TextField()
    license_short_name = models.TextField()
    attribution = models.TextField(null=True, blank=True)
    license_url = models.URLField(null=True, blank=True)
    attribution_required = models.BooleanField()
    copyrighted = models.BooleanField()
    timestamp = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        img = WikipediaImageAPIObject(self.filename)
        self.thumbnail.delete(save=False)
        print("saving")
        with TemporaryFile("rb+") as fd:
            r = requests.get(img.thumburl)
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
            image_file = File(fd)
            self.thumbnail.save(self.filename, image_file, save=False)
        self.thumb_width, self.thumb_height = img.thumb_size
        self.pageid = img.pageid
        self.imageurl = img.url
        self.credit = img.credit
        self.artist = img.artist
        self.license_short_name = img.license_short_name
        self.attribution = img.attribution
        self.license_url = img.license_url
        self.attribution_required = img.attribution_required
        self.copyrighted = img.copyrighted
        self.timestamp = img.timestamp

        super(WikipediaImage, self).save(*args, **kwargs)

    @property
    def commons_url(self):
        return f"https://commons.wikimedia.org/wiki/File:{self.filename}"

    def __str__(self):
        return self.filename
