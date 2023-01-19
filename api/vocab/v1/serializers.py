from rest_framework import serializers

from vocab.models import VocabSource, Page, Word


class VocabSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VocabSource
        fields = ("id", "source", "url")


class PageSerializer(serializers.ModelSerializer):
    words = serializers.StringRelatedField(many=True, read_only=True, source="word_set")

    class Meta:
        model = Page
        fields = ("id", "page", "words")


class VocabWordSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, source="page_set")

    class Meta:
        model = VocabSource
        fields = "__all__"


class PageHyperLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Page
        fields = ("id", "page", "url")


class VocabSourcePageSerializer(serializers.HyperlinkedModelSerializer):
    pages = PageHyperLinkSerializer(many=True, source="page_set")

    class Meta:
        model = VocabSource
        fields = ("id", "source", "sheet", "pages")
