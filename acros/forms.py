from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, CharField

from acros.models import Acronym, Tag, WikipediaLink, PaperReference, Weblink
from acros.utils.tags import parse_tags, edit_string_for_tags


class TagWidget(TextInput):
    def format_value(self, value):
        if value is not None and not isinstance(value, str):
            value = edit_string_for_tags(value)
        return super().format_value(value)

    def __init__(self, *args, **kwargs):
        super(TagWidget, self).__init__(*args, **kwargs)
        attrs = {"class": "taginput"}
        self.attrs.update(attrs)


class TagField(CharField):
    """
    based on https://github.com/jazzband/django-taggit/blob/master/taggit/models.py

    """
    widget = TagWidget

    def clean(self, value):
        value = super().clean(value)
        try:
            tag_strings = parse_tags(value)
            tag_ids = []
            for tag in tag_strings:
                try:
                    to = Tag.objects.get(name__iexact=tag)
                except Tag.DoesNotExist:
                    to = Tag(name=tag)
                    to.save()
                tag_ids.append(to.pk)
            return tag_ids
        except ValueError:
            raise ValidationError(
                "Please provide a comma-separated list of tags."
            )


class EditForm(ModelForm):
    tags = TagField()

    class Meta:
        model = Acronym
        fields = ['name', 'full_name', "description_md", "stub", "tags"]


class EditLetterForm(ModelForm):
    class Meta:
        model = Acronym
        fields = ["acro_letters"]


class AddForm(ModelForm):
    tags = TagField()

    class Meta:
        model = Acronym

        fields = ['name', 'full_name', "description_md", "stub", "tags"]


class WikipediaForm(ModelForm):
    class Meta:
        model = WikipediaLink

        fields = ['title']


class PaperForm(ModelForm):
    class Meta:
        model = PaperReference

        fields = ['bibcode']


class WeblinkForm(ModelForm):
    class Meta:
        model = Weblink

        fields = ['url']
