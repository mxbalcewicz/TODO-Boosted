from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required, name="dispatch")
class DashboardView(TemplateView):
    view_name = "dashboard"
    template_name = "dashboard.html"
