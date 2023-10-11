from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View


class BoostedAbstractView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BoostedAbstractView, self).dispatch(*args, **kwargs)

    # Used in url routing in reverse method
    @classmethod
    def get_view_name(cls):
        return f"{cls.app_name}:{cls.view_name}"
