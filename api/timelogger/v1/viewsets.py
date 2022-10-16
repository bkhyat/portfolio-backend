from datetime import timedelta
from itertools import groupby

import django_filters
from django.db.models import Max
from rest_framework import filters
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(methods=['GET'], detail=False, url_path='weekly-summary')
    def weekly_summary(self, request, *args, **kwargs):
        """
        Always considers the maximum date as the current week.
        ToDo: May need to allow query param to pass two different weeks of the years and filter accordingly
        """
        qs = self.get_queryset()
        last_date = qs.aggregate(Max('date'))['date__max']
        current = last_date - timedelta(days=last_date.weekday())
        prev = current - timedelta(days=7)
        current_week = qs.filter(date__lte=last_date, date__gte=current)
        prev_week = qs.filter(date__lt=current, date__gte=prev)

        return Response({'this_week': {k: sum(obj.duration_in_minutes for obj in v) for k, v in
                                       groupby(current_week, key=lambda x: x.date.weekday())},
                         'prev_week': {k: sum(obj.duration_in_minutes for obj in v) for k, v in
                                       groupby(prev_week, key=lambda x: x.date.weekday())}
                         })
