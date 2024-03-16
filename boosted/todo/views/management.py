from django.views.generic import ListView, TemplateView
from todo.forms import TODOFilterForm
from todo.views import TODOGenericView
from tools.views import GenericQueryParamsMixin


class TODOBaseView(TODOGenericView, TemplateView):
    view_name = "todo_base"
    template_name = "todo_base.html"


class TODOManagementViewQueryParamsMixin(GenericQueryParamsMixin):
    param_key = "todo:todo_management"

    def make_query_params(self, form_data):
        params = "?"
        for key, value in form_data.items():
            params += f"{key}={value}"
        return params


class TODOManagementView(TODOGenericView, ListView, TODOManagementViewQueryParamsMixin):
    view_name = "todo_management"
    template_name = "todo_management.html"
    form_class = TODOFilterForm

    def get_filter_form(self, **kwargs):
        return self.form_class(data=self.request.GET or None, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if not self.filter_form:
            self.filter_form = self.get_filter_form(**self.get_form_kwargs())
        data["filter_form"] = self.filter_form
        data["context"] = self.filter_form.context
        return data

    def get_queryset(self):
        self.filter_form = self.get_filter_form(**self.get_form_kwargs())
        if self.filter_form.is_valid():
            params = self.make_query_params(self.filter_form.cleaned_data)
            self.save_query_params_to_session(params)
        return self.filter_form.get_queryset()

    def get_form_kwargs(self):
        return {"user": self.request.user}
