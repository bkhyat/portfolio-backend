from rest_framework import serializers

from timelogger.models import TimeLog


class TimeLoggerSerializer(serializers.ModelSerializer):
    duration = serializers.ReadOnlyField()

    class Meta:
        model = TimeLog
        fields = '__all__'
        read_only_fields = ('user',)
