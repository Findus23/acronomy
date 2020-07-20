from django.core.management.base import BaseCommand
from django.db import transaction

from acronomy.settings import DEBUG
from acros.models import Acronym
from acros.utils.matomo import fetch_matomo_pages


class Command(BaseCommand):
    help = 'Fetches Acronym Popularity from Matomo'

    def handle(self, *args, **options):
        with transaction.atomic():
            for pagestat in fetch_matomo_pages():
                url: str = pagestat["label"]
                if not url.startswith("/acronym/"):
                    continue
                fragments = url.split("/")
                if len(fragments) != 3:
                    continue
                slug = fragments[2]
                try:
                    acronym = Acronym.objects.get(slug=slug)
                except Acronym.DoesNotExist:
                    if DEBUG:
                        continue
                    else:
                        raise
                print(acronym)
                views = pagestat["nb_visits"]
                acronym.pageviews = views
                acronym.save()
