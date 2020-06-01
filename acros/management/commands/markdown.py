from django.core.management.base import BaseCommand

from acros.models import Acronym
from acros.utils import md_to_html


class Command(BaseCommand):
    help = 'Updates all Markdown descriptions'

    def handle(self, *args, **options):
        acronyms = Acronym.objects.all()
        for acronym in acronyms:
            print(acronym.name)
            acronym.description_html = md_to_html(acronym.description_md)
