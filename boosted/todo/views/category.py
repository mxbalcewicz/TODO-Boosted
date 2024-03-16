from django.urls import reverse
from django.views.generic import DeleteView
from todo.forms import TaskCategoryForm
from todo.models import TaskCategory
from todo.views import TODOGenericView
from todo.views.management import (
    TODOManagementView,
    TODOManagementViewQueryParamsMixin,
)
from tools.views import GenericCreateView, GenericDetailView


class TaskCategoryCreateView(TODOGenericView, GenericCreateView):
    view_name = "category_create"
    form_class = TaskCategoryForm
    form_title = "New task category"
    list_url = "todo:todo_management"

    def get_success_url(self):
        return reverse(TODOManagementView.get_view_name() + "?model=Category")


class TaskCategoryDetailView(
    TODOGenericView, GenericDetailView, TODOManagementViewQueryParamsMixin
):
    view_name = "category_detail"
    model = TaskCategory
    list_url = "todo:todo_management"
    delete_url = "todo:category_delete"
    field_lookup_map = {"ID": "pk", "Name": "name", "Color": "color"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query_params"] = self.get_query_params()
        return context


class TaskCategoryDeleteView(TODOGenericView, DeleteView):
    view_name = "category_delete"
    model = TaskCategory

    def get_success_url(self) -> str:
        return reverse(TODOManagementView.get_view_name()) + "?model=Category"
