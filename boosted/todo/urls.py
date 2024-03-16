from django.urls import re_path
from todo.views import (
    CategoryCreateView,
    CategoryDetailView,
    TaskBoardCreateView,
    TaskBoardDeleteView,
    TaskBoardDetailView,
    TaskCategoryDeleteView,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TODOBaseView,
    TODOBoardListView,
    TODOManagementView,
)

urlpatterns = [
    re_path(r"^$", TODOBaseView.as_view(), name=TODOBaseView.view_name),
    re_path(r"^task/new$", TaskCreateView.as_view(), name=TaskCreateView.view_name),
    re_path(
        r"^category/new$",
        CategoryCreateView.as_view(),
        name=CategoryCreateView.view_name,
    ),
    re_path(
        r"^board/new$",
        TaskBoardCreateView.as_view(),
        name=TaskBoardCreateView.view_name,
    ),
    re_path(
        r"^category/(?P<pk>\d+)/$",
        CategoryDetailView.as_view(),
        name=CategoryDetailView.view_name,
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
        r"^boards/$", TODOBoardListView.as_view(), name=TODOBoardListView.view_name
    ),
    re_path(
        r"management/", TODOManagementView.as_view(), name=TODOManagementView.view_name
    ),
]
