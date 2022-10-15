from django.db.models import Sum
from rest_framework import serializers

from backend.core.utils import convert_minutes_to_time
from timelogger.models import TimeLog


class TimeLoggerSerializer(serializers.ModelSerializer):
    duration_in_minutes = serializers.ReadOnlyField()
    # total = serializers.SerializerMethodField()

    class Meta:
        model = TimeLog
        fields = '__all__'
        read_only_fields = ('user',)
