from django.urls import re_path
from todo.views import TODOBaseView, TODOBoardListView, TODOManagementView

urlpatterns = [
    re_path(r"^$", TODOBaseView.as_view(), name=TODOBaseView.view_name),
    re_path(r"board/", TODOBoardListView.as_view(), name=TODOBoardListView.view_name),
    re_path(
        r"management/", TODOManagementView.as_view(), name=TODOManagementView.view_name
    ),
]
