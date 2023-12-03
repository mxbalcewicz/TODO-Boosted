from admin_panel.views import UsersManagementListView
from django.urls import re_path

urlpatterns = [
    re_path(
        r"users_list",
        UsersManagementListView.as_view(),
        name=UsersManagementListView.view_name,
    ),
]
