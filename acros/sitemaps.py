from django.contrib.sitemaps import Sitemap

from .models import Acronym


class AcronymSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Acronym.objects.all()

    def lastmod(self, obj: Acronym):
        return obj.modified_date
