from django.core.management.base import BaseCommand
from simple_history.utils import update_change_reason

from acros.models import WikipediaLink


class Command(BaseCommand):
    help = 'Updates all Wikipedia articles'

    def handle(self, *args, **options):
        links = WikipediaLink.objects.all()
        for link in links:
            if link.fetched:
                self.stdout.write(link.title)
                link.fetched = False
                # update_change_reason(link, "refetch_wikipedia command")
                link.save()
