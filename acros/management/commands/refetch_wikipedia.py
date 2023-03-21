import time

from django.core.management.base import BaseCommand

from acros.models import WikipediaLink


class Command(BaseCommand):
    help = 'Updates all Wikipedia articles'

    def handle(self, *args, **options):
        links = WikipediaLink.objects.all()
        for link in links:
            print(link)
            self.stdout.write(link.title)
            link.fetched = False
            # update_change_reason(link, "refetch_wikipedia command")
            link.clean()
            link.save()
            time.sleep(1)
