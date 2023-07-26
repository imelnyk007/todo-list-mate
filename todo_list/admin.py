from django.contrib import admin
from django.contrib.auth.models import Group

from todo_list.models import Tag, Task

admin.site.unregister(Group)

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "completed")
