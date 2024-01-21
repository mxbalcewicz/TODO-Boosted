from accounts.views import (
    SettingsEditView,
    SettingsView,
    UsersManagementListView
)
from django.urls import re_path

urlpatterns = [
    re_path(
        r"settings/(?P<pk>\d+)/?$",
        view=SettingsView.as_view(),
        name=SettingsView.view_name,
    ),
    re_path(
        r"settings/edit/(?P<pk>\d+)/?$",
        view=SettingsEditView.as_view(),
        name=SettingsEditView.view_name,
    ),
    re_path(
        r"users_list",
        UsersManagementListView.as_view(),
        name=UsersManagementListView.view_name,
    ),
]
