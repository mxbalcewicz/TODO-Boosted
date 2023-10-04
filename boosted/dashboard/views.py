from django.views.generic import TemplateView
from tools.views import BoostedAbstractView


class DashboardView(BoostedAbstractView, TemplateView):
    view_name = "dashboard"
    template_name = "dashboard.html"
