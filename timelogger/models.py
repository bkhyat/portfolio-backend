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