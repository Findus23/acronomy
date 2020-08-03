from acros.models import Tag
from acros.utils.checks import BaseCheck, CheckWarning, registry


class TagsCheck(BaseCheck):
    def run(self):
        for tag in Tag.objects.filter(acronyms=None):
            yield CheckWarning(
                "Tag is unused",
                obj=tag)


registry.register(TagsCheck)
