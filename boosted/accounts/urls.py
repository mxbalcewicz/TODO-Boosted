from accounts.views import SettingsView
from django.urls import re_path

urlpatterns = [
    re_path(
        r"settings/(?P<pk>\d+)/?$",
        view=SettingsView.as_view(),
        name=SettingsView.view_name,
    ),
]
