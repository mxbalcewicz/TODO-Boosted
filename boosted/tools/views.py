from typing import Any

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, View


class BoostedAbstractView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BoostedAbstractView, self).dispatch(*args, **kwargs)

    # Used in url routing in reverse method
    @classmethod
    def get_view_name(cls):
        return f"{cls.app_name}:{cls.view_name}"


class GenericCreateView(CreateView):
    template_name = "generic_create.html"
    form_title = None
    back_url = None

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_title"] = self.form_title
        context["back_url"] = self.back_url
        return context
