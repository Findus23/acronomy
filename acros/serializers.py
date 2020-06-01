from rest_framework import serializers

from acros.models import Acronym, Weblink, PaperReference, Tag, WikipediaLink


class WeblinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weblink
        exclude = ["acronym"]


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperReference
        fields = ["title", "bibcode", "arxiv_id", "doi", "ads_url", "arxiv_url", "doi_url"]


class WikipediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikipediaLink
        fields = ["title", "url"]


class AcronymListSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Acronym
        exclude = ['description_md']


class AcronymSerializer(serializers.HyperlinkedModelSerializer):
    # links = serializers.SlugRelatedField(many=True,read_only=True,slug_field="url")
    links = WeblinkSerializer(many=True)
    papers = PaperSerializer(many=True)
    wiki_articles = WikipediaSerializer(many=True)
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Acronym
        exclude = ['description_md']
        # fields = ["name", "links","dois"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]
