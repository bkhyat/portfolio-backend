from rest_framework import serializers

from vocab.models import VocabSource, Page, Word, Category, VocabWord


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


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = "__all__"


class PracticeSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

    def get_data(self, instance):
        data = {"id": instance.id, "category_name": instance.category_name}
        if children := [
            PracticeSetSerializer.get_data(self, child)
            for child in instance.children.all()
        ]:
            data["children"] = children
        return data

    def to_representation(self, instance):
        return self.get_data(instance)


class CategoryWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = VocabWord
        fields = "__all__"

