from django.core.exceptions import ValidationError
from django.db import models
from django.dispatch import receiver

from acros.models import Acronym, WikipediaLink


@receiver(models.signals.post_save, sender=Acronym)
def execute_after_save(sender: Acronym, instance: Acronym, created: bool, *args, **kwargs):
    if created:
        try:
            link = WikipediaLink()
            link.title = instance.full_name
            link.acronym = instance
            link.clean()
            link.save()
        except ValidationError:
            pass
