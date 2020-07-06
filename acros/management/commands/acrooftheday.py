from datetime import date, timedelta

from django.core.management.base import BaseCommand

from acros.models import Acronym, AcroOfTheDay


class Command(BaseCommand):
    help = 'Selects Acronym of the Day for the next day'

    def handle(self, *args, **options):
        today = date.today()
        tomorrow = today + timedelta(days=1)
        AcroOfTheDay.objects.filter(date__gt=today).delete()
        AcroOfTheDay.objects.filter(date__lt=today).delete()
        selected = Acronym.objects.order_by('?')[:5]
        for i,acr in enumerate(selected):
            AcroOfTheDay.objects.create(acronym=acr, date=tomorrow,order=i)
            print(acr.name)
