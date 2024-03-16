from django.urls import reverse
from django.views.generic import DeleteView, FormView
from todo.forms import TaskBoardForm, TaskBoardHiddenForm
from todo.models import TaskBoard
from todo.views import TODOGenericView
from todo.views.management import (
    TODOManagementView,
    TODOManagementViewQueryParamsMixin,
)
from tools.views import GenericCreateView, GenericDetailView


class TaskBoardListView(TODOGenericView, FormView):
    view_name = "board_list"
    template_name = "board_list.html"
    model = TaskBoard
    form_class = TaskBoardHiddenForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse(self.get_view_name())

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskBoardCreateView(TODOGenericView, GenericCreateView):
    view_name = "board_create"
    form_class = TaskBoardForm
    form_title = "New task board"
    list_url = "todo:todo_management"

    def get_success_url(self):
        return reverse(TODOManagementView.get_view_name() + "?model=Board")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class TaskBoardDetailView(
    TODOGenericView, GenericDetailView, TODOManagementViewQueryParamsMixin
):
    view_name = "board_detail"
    model = TaskBoard
    list_url = "todo:todo_management"
    delete_url = "todo:board_delete"
    field_lookup_map = {"ID": "pk", "Name": "name", "Tasks": "tasks"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query_params"] = self.get_query_params()
        return context


class TaskBoardDeleteView(TODOGenericView, DeleteView):
    view_name = "board_delete"
    model = TaskBoard

    def get_success_url(self) -> str:
        return reverse(TODOManagementView.get_view_name()) + "?model=Board"
