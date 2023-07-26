from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    success_url = reverse_lazy("togo_list:tag-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    success_url = reverse_lazy("togo_list:task-list")
