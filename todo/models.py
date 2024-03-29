from django.db import models


class TimeStampModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ToDo(TimeStampModel):
    class Meta:
        ordering = ['is_completed', '-updated_at', '-created_at']

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True)


class Test_Model(models.Model):
    Name = models.CharField(max_length=1, default='')
    Value = models.IntegerField(default=1)
