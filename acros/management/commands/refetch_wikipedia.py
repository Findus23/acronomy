from django.core.management.base import BaseCommand

from acros.models import WikipediaLink


class Command(BaseCommand):
    help = 'Updates all Wikipedia articles'

    def handle(self, *args, **options):
        links = WikipediaLink.objects.all()
        for link in links:
            if link.fetched:
                self.stdout.write(link.title)
                link.fetched = False
                link.save()
