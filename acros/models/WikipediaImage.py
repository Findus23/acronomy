from tempfile import TemporaryFile

from django.core.files import File
from django.db import models

from acros.utils.apis import WikipediaImageAPIObject, NotFoundError, requests_session


class WikipediaImage(models.Model):
    filename = models.CharField(max_length=200)
    pageid = models.IntegerField(editable=False)
    thumbnail = models.ImageField(upload_to="wikipedia_images/", blank=True, null=True, editable=False)
    thumb_width = models.IntegerField(blank=True, editable=False, null=True)
    thumb_height = models.IntegerField(blank=True, editable=False, null=True)
    imageurl = models.URLField(editable=False)
    caption = models.CharField(max_length=1000, null=True, blank=True)
    credit = models.TextField(null=True, blank=True, editable=False)
    artist = models.TextField(null=True, blank=True, editable=False)
    license_short_name = models.TextField(editable=False)
    attribution = models.TextField(null=True, blank=True, editable=False)
    license_url = models.URLField(null=True, blank=True, editable=False)
    attribution_required = models.BooleanField(editable=False)
    copyrighted = models.BooleanField(editable=False)
    timestamp = models.DateTimeField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        try:
            img = WikipediaImageAPIObject(self.filename)
        except NotFoundError:
            return False
        if self.thumbnail:
            self.thumbnail.delete(save=False)
        print("saving")
        filename = self.filename
        if filename.endswith(".svg"):
            filename += ".png"
        with TemporaryFile("rb+") as fd:
            r = requests_session.get(img.thumburl)
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
            image_file = File(fd)
            self.thumbnail.save(filename, image_file, save=False)
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
        return True

    @property
    def commons_url(self):
        return f"https://commons.wikimedia.org/wiki/File:{self.filename}"

    def __str__(self):
        return self.filename
