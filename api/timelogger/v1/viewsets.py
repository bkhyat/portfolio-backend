import django_filters
from django.db.models import Sum
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import filters

from api.timelogger.v1.serializers import TimeLoggerSerializer
from timelogger.models import TimeLog


class TimeLoggerViewSet(viewsets.ModelViewSet):
    serializer_class = TimeLoggerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date']
    search_fields = ['description']
    # queryset = TimeLog.objects.all()

    # def filter_queryset(self, queryset):
    #     pass

    def get_queryset(self):
        return TimeLog.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(user=request.user)
        return Response(self.serializer_class(instance).data)

    def list(self, request, *args, **kwargs):
        return super(TimeLoggerViewSet, self).list(request, *args, **kwargs)


