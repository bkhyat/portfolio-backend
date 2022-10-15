from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from backend.core.utils import convert_minutes_to_time


class TimeLog(models.Model):
    date = models.DateField(verbose_name='Date')
    start = models.TimeField(verbose_name='Start Time')
    end = models.TimeField(verbose_name='End Time')
    description = models.CharField(max_length=500, verbose_name='Log')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date', 'start']
        get_latest_by = ['-date', '-start']

    def __str__(self) -> str:
        return f"{self.date}. {self.start}-{self.end} ({self.duration})"

    @property
    def duration(self) -> str:
        return convert_minutes_to_time(self.duration_in_minutes)

    @property
    def duration_in_minutes(self) -> int:
        # May need to revisit if start and end times can be in different days
        start = timedelta(hours=self.start.hour, minutes=self.start.minute)
        end = timedelta(hours=self.end.hour, minutes=self.end.minute)
        minutes = int((end - start).total_seconds() // 60)
        return minutes
