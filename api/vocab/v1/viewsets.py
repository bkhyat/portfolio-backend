from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.vocab.v1.serializers import VocabWordSerializer, VocabSourceSerializer, VocabSourcePageSerializer, \
    PageHyperLinkSerializer, PageSerializer
from vocab.models import Word, VocabSource, Page


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
        return Response(data=[str(word) for word in Word.objects.order_by('?').distinct("word")[:3].values_list("word", flat=True)])
    

class PageViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageHyperLinkSerializer
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return PageSerializer

        return super(PageViewset, self).get_serializer_class()
