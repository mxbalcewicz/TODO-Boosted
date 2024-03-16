from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, View


class BoostedAbstractView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BoostedAbstractView, self).dispatch(*args, **kwargs)

    # Used in url routing in reverse method
    @classmethod
    def get_view_name(cls):
        return f"{cls.app_name}:{cls.view_name}"


class GenericQueryParamsMixin:
    param_key = None

    def save_query_params_to_session(self, data):
        self.request.session[self.param_key] = data

    def get_query_params(self):
        return self.request.session.get(self.param_key, "")

    def make_query_params(self):
        raise Exception("Method not implemented.")


class GenericCreateView(CreateView):
    template_name = "generic_create.html"
    form_title = None
    list_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = self.form_title
        context["list_url"] = self.list_url
        return context


class GenericDetailView(DetailView):
    template_name = "generic_detail.html"
    field_lookup_map = {}
    list_url = None
    edit_url = None
    delete_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field_lookup_map"] = self.field_lookup_map
        context["list_url"] = self.list_url
        context["edit_url"] = self.edit_url
        context["delete_url"] = self.delete_url
        return context
