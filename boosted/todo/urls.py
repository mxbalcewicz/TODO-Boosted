from django.urls import re_path
from todo.views import (
    CategoryCreateView,
    TaskCreateView,
    TODOBaseView,
    TODOBoardListView,
    TODOManagementView,
)

urlpatterns = [
    re_path(r"^$", TODOBaseView.as_view(), name=TODOBaseView.view_name),
    re_path(r"^new_task$", TaskCreateView.as_view(), name=TaskCreateView.view_name),
    re_path(
        r"^new_category$",
        CategoryCreateView.as_view(),
        name=CategoryCreateView.view_name,
    ),
    re_path(
        r"^boards/$", TODOBoardListView.as_view(), name=TODOBoardListView.view_name
    ),
    re_path(
        r"management/", TODOManagementView.as_view(), name=TODOManagementView.view_name
    ),
]
