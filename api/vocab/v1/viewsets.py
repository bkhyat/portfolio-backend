import math
import random
import datetime

from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from api.vocab.utils import WordPagination
from api.vocab.v1.serializers import VocabWordSerializer, VocabSourceSerializer, VocabSourcePageSerializer, \
    PageHyperLinkSerializer, PageSerializer, WordSerializer, PracticeSetSerializer, CategoryWordSerializer
from vocab.models import Word, VocabSource, Page, Category


class VocabViewset(viewsets.ReadOnlyModelViewSet):
    model = VocabSource
    queryset = VocabSource.objects.all()
    serializer_class = VocabSourceSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return VocabSourcePageSerializer

        return super(VocabViewset, self).get_serializer_class()

    @action(detail=True, url_path="words")
    def get_words_by_sheet(self, request, pk, *args, **kwargs):
        return Response(data=[str(word) for word in Word.objects.filter(page__vocab_source=pk).distinct("word").values_list("word", flat=True)])

    @action(detail=False, url_path="words-of-the-day")
    def get_random_3_words(self, request, *args, **kwargs):
        today = datetime.date.today()
        random.seed(today.year + today.month + today.day+3)
        words = list(Word.objects.distinct("word").values_list("word", flat=True))
        return Response(data=random.choices(words, k=3))


class PageViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageHyperLinkSerializer
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return PageSerializer

        return super(PageViewset, self).get_serializer_class()


class WordViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Word.objects.all()
    pagination_class = WordPagination
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        if request.GET.get("only_page_count", False):
            return Response(data={
                "page_count": math.ceil(self.get_queryset().count() / self.pagination_class.page_size)})
        return super().list(self, request, *args, **kwargs)


class VocabPracticeViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = PracticeSetSerializer
    queryset = Category.objects.filter(parent_category__isnull=True)

    @action(["GET"], True)
    def words(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        qs = category.get_associated_words()
        serializer = CategoryWordSerializer(qs, many=True)
        return Response(data=serializer.data)
