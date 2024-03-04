from dashboard.views import DashboardView
from django.urls import re_path

urlpatterns = [
    re_path(r"", DashboardView.as_view(), name=DashboardView.view_name),
]
