from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class TimeLog(models.Model):
    date = models.DateField(verbose_name='Date')
    start = models.TimeField(verbose_name='Start Time')
    end = models.TimeField(verbose_name='End Time')
    description = models.CharField(max_length=500, verbose_name='Log')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date', 'start']
        get_latest_by = ['-date', '-start']

    def __str__(self):
        return f"{self.date}. {self.start}-{self.end} ({self.duration})"

    @property
    def duration(self):
        # May need to revisit if start and end times can be in different days
        start = timedelta(hours=self.start.hour, minutes=self.start.minute)
        end = timedelta(hours=self.end.hour, minutes=self.end.minute)
        minutes = (end-start).total_seconds()//60
        hrs = int(minutes // 60)
        minutes = int(minutes - hrs*60)
        if hrs:
            return f"{hrs}H {minutes}M"

        return f"{minutes}M"
