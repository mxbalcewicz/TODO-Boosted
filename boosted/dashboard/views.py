from django.views.generic import TemplateView
from tools.views import BoostedAbstractView


class DashBoardGenericView(BoostedAbstractView):
    app_name = "dashboard"


class DashboardView(DashBoardGenericView, TemplateView):
    view_name = "dashboard"
    template_name = "dashboard.html"
