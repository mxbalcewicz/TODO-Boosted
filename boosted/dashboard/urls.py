from dashboard.views import DashboardView
from django.urls import re_path

# from django.contrib import admin

urlpatterns = [
    re_path(r"^$", DashboardView.as_view(), name="dashboard"),
]
