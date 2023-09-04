from dashboard.views import DashboardView
from django.urls import re_path

# from django.contrib import admin

app_name = "dashboard"

urlpatterns = [
    re_path(r"^dashboard$", DashboardView.as_view(), name="dashboard"),
]
