from django.contrib import admin
from todo.models import ToDo
# Register your models here.


class ToDoAdmin(admin.ModelAdmin):
    pass


admin.site.register(ToDo, ToDoAdmin)
