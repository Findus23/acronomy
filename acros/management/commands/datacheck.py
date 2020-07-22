from django.core.management.base import BaseCommand

from acros.utils.checks import registry


class Command(BaseCommand):
    help = 'check integrity of data'

    def handle(self, *args, **kwargs):
        errors = registry.run_checks()
        for error in errors:
            print(error)
