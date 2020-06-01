from io import BytesIO
from tempfile import TemporaryFile

import requests
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models


class Host(models.Model):
    host = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="host_icons/", blank=True,
                             height_field="icon_height", width_field="icon_width")
    icon_width = models.IntegerField(blank=True, null=True, editable=False)
    icon_height = models.IntegerField(blank=True, null=True, editable=False)
    fetched = models.BooleanField(default=False)

    def __str__(self):
        return self.host

    def save(self, *args, **kwargs):
        if not self.fetched or True:
            with TemporaryFile("rb+") as fd:
                r = requests.get(f"https://external-content.duckduckgo.com/ip3/{self.host}.ico")
                if r.status_code == 200:
                    filename = self.host + ".png"
                    for chunk in r.iter_content(chunk_size=128):
                        fd.write(chunk)
                    image = Image.open(fd)
                    image_io = BytesIO()
                    image.save(image_io, format='PNG', quality=9)
                    self.icon.save(filename, ContentFile(image_io.getvalue()), save=False)
                else:
                    self.icon = None
            self.fetched = True

        super(Host, self).save(*args, **kwargs)
