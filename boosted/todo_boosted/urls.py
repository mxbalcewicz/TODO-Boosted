from accounts.views import BoostedLoginView, RegisterView
from django.urls import include, re_path

# from django.contrib import admin

urlpatterns = [
    re_path(r"^", include("dashboard.urls")),
    re_path(r"^login/$", view=BoostedLoginView.as_view(), name="login"),
    re_path(r"^register/$", view=RegisterView.as_view(), name="register"),
]
