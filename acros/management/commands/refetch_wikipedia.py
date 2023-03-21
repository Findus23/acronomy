import time
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from acros.models import WikipediaLink


class Command(BaseCommand):
    help = 'Updates all Wikipedia articles'

    def handle(self, *args, **options):
        links = WikipediaLink.objects.all()
        for link in links:
            self.stdout.write(link.title)
            if link.timestamp >= (timezone.now() - timedelta(days=180)):
                print("skipped")
                continue
            link.fetched = False
            # update_change_reason(link, "refetch_wikipedia command")
            link.clean()
            link.save()
            time.sleep(3)
