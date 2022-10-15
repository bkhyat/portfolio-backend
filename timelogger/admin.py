from django.contrib import admin

# Register your models here.
from timelogger.models import TimeLog


class TimeLoggerAdmin(admin.ModelAdmin):
    pass


admin.site.register(TimeLog, TimeLoggerAdmin)
