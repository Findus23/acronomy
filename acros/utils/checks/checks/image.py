from acros.models import WikipediaImage
from acros.utils.checks import BaseCheck, CheckWarning, registry


class AuthorAttributionCheck(BaseCheck):
    def run(self):
        for image in WikipediaImage.objects.all():
            if image.attribution_required and not image.artist:
                yield CheckWarning("Image needs attribution, but is missing an artist", obj=image)


registry.register(AuthorAttributionCheck)

