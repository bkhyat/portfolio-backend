from django.db.models import Sum
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from backend.core.utils import convert_minutes_to_time
from timelogger.models import TimeLog


class TimeLoggerSerializer(serializers.ModelSerializer):
    duration_in_minutes = serializers.ReadOnlyField()
    # total = serializers.SerializerMethodField()

    class Meta:
        model = TimeLog
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, attrs):
        # Validate if start time is less than end time
        if attrs['start'] > attrs['end']:
            raise ValidationError({"start": "Start Time can not be Greater than End Time"})
        # Add validation to check if date is not greater than today, i.e. you can not add log for future
        # Same may be applicable for start and end too
        # And it may require to use UTC as time can differ from server to clients
        return super(TimeLoggerSerializer, self).validate(attrs)
