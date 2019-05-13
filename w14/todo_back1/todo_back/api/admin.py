from django.contrib import admin
from . import models

admin.site.register(models.Task)

@admin.register(models.TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', )