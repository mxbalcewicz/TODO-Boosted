from accounts import urls as accounts_urls
from accounts.views import BoostedLoginView, LogoutView, RegisterView
from dashboard import urls as dashboard_urls
from django.urls import include, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(r"^$", view=RedirectView.as_view(url="login"), name="root"),
    re_path(
        r"^login/$", view=BoostedLoginView.as_view(), name=BoostedLoginView.view_name
    ),
    re_path(r"^logout/$", view=LogoutView.as_view(), name=LogoutView.view_name),
    re_path(r"^register/$", view=RegisterView.as_view(), name=RegisterView.view_name),
    re_path(r"^dashboard/", include((dashboard_urls, "dashboard"))),
    re_path(r"^accounts/", include((accounts_urls, "accounts"))),
]
