from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Acronym, Tag


class AcronymSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Acronym.objects.all()

    def lastmod(self, obj: Acronym):
        return obj.modified_date


class TagsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Tag.objects.all()


class StaticPagesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return [
            reverse("index"),
            reverse("overview"),
            reverse("tags"),
            reverse("integrations")
        ]

    def location(self, url):
        return url
