from django.urls import re_path
from todo.views.board import (
    TaskBoardCreateView,
    TaskBoardDeleteView,
    TaskBoardDetailView,
    TaskBoardListView,
)
from todo.views.category import (
    TaskCategoryCreateView,
    TaskCategoryDeleteView,
    TaskCategoryDetailView,
)
from todo.views.management import TODOBaseView, TODOManagementView
from todo.views.task import TaskCreateView, TaskDeleteView, TaskDetailView

urlpatterns = [
    re_path(r"^$", TODOBaseView.as_view(), name=TODOBaseView.view_name),
    re_path(r"^task/new$", TaskCreateView.as_view(), name=TaskCreateView.view_name),
    re_path(
        r"^category/new$",
        TaskCategoryCreateView.as_view(),
        name=TaskCategoryCreateView.view_name,
    ),
    re_path(
        r"^board/new$",
        TaskBoardCreateView.as_view(),
        name=TaskBoardCreateView.view_name,
    ),
    re_path(
        r"^category/(?P<pk>\d+)/$",
        TaskCategoryDetailView.as_view(),
        name=TaskCategoryDetailView.view_name,
    ),
    re_path(
        r"^task/(?P<pk>\d+)/$", TaskDetailView.as_view(), name=TaskDetailView.view_name
    ),
    re_path(
        r"^board/(?P<pk>\d+)/delete/$",
        TaskBoardDeleteView.as_view(),
        name=TaskBoardDeleteView.view_name,
    ),
    re_path(
        r"^category/(?P<pk>\d+)/delete/$",
        TaskCategoryDeleteView.as_view(),
        name=TaskCategoryDeleteView.view_name,
    ),
    re_path(
        r"^task/(?P<pk>\d+)/delete/$",
        TaskDeleteView.as_view(),
        name=TaskDeleteView.view_name,
    ),
    re_path(
        r"^board/(?P<pk>\d+)/$",
        TaskBoardDetailView.as_view(),
        name=TaskBoardDetailView.view_name,
    ),
    re_path(
        r"^boards/$", TaskBoardListView.as_view(), name=TaskBoardListView.view_name
    ),
    re_path(
        r"management/", TODOManagementView.as_view(), name=TODOManagementView.view_name
    ),
]
