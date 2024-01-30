from accounts.views import (
    SettingsEditView,
    SettingsView,
    UsersManagementListView,
    GroupsManagementListView,
    GroupDetailView,
    GroupUpdateView
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
    re_path(
        r"groups_list",
        GroupsManagementListView.as_view(),
        name=GroupsManagementListView.view_name,
    ),
    re_path(
        r"group/(?P<pk>\d+)/?$",
        GroupDetailView.as_view(),
        name=GroupDetailView.view_name,
    ),
    re_path(
        r"group/edit/(?P<pk>\d+)/?$",
        GroupUpdateView.as_view(),
        name=GroupUpdateView.view_name,
    ),
]
