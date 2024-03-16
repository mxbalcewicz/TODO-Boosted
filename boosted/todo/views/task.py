from django.urls import reverse
from django.views.generic import DeleteView
from todo.forms import TaskForm
from todo.models import Task
from todo.views import TODOGenericView
from todo.views.management import (
    TODOManagementView,
    TODOManagementViewQueryParamsMixin,
)
from tools.views import GenericCreateView, GenericDetailView


class TaskCreateView(TODOGenericView, GenericCreateView):
    view_name = "task_create"
    form_class = TaskForm
    form_title = "New task"
    list_url = "todo:todo_management"

    def get_success_url(self):
        return reverse(TODOManagementView.get_view_name() + "?model=Task")


class TaskDetailView(
    TODOGenericView, GenericDetailView, TODOManagementViewQueryParamsMixin
):
    view_name = "task_detail"
    model = Task
    list_url = "todo:todo_management"
    delete_url = "todo:task_delete"
    field_lookup_map = {
        "ID": "pk",
        "Name": "name",
        "Description": "description",
        "Category": "category__name",
        "Created at": "created_at",
        "Completed": "completed",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query_params"] = self.get_query_params()
        return context


class TaskDeleteView(TODOGenericView, DeleteView):
    view_name = "task_delete"
    model = Task

    def get_success_url(self) -> str:
        return reverse(TODOManagementView.get_view_name()) + "?model=Task"
