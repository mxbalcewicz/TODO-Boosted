from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from tools.views import BoostedAbstractView


class DashboardGenericView(BoostedAbstractView):
    app_name = "dashboard"


@method_decorator(login_required, name="dispatch")
class DashboardView(DashboardGenericView, TemplateView):
    view_name = "dashboard"
    template_name = "dashboard.html"
