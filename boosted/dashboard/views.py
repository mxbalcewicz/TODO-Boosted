from typing import Any

from dashboard.models import AppLabel
from django.views.generic import TemplateView
from tools.views import BoostedAbstractView


class DashBoardGenericView(BoostedAbstractView):
    app_name = "dashboard"


class DashboardView(DashBoardGenericView, TemplateView):
    view_name = "dashboard"
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data["apps"] = AppLabel.objects.all()
        return data
