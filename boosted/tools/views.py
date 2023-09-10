from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View


class BoostedAbstractView(View):
    view_name = ""
    template_name = ""
    app_name = ""

    @classmethod
    def get_view_name(cls):
        return f"{cls.app_name}:{cls.view_name}"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BoostedAbstractView, self).dispatch(*args, **kwargs)
