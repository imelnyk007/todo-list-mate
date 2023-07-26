from django.urls import path

from todo_list.views import TagListView, TaskListView, TagCreateView, TagUpdateView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("/create", TaskCreateView.as_view(), name="task-create"),
    path("/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]

app_name = "todo_list"
