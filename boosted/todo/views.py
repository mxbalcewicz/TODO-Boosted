from typing import Any

from django.urls import reverse
from django.views.generic import FormView, ListView, TemplateView
from todo.forms import (
    TaskBoardHiddenForm,
    TaskCategoryForm,
    TaskForm,
    TODOFilterForm,
)
from todo.models import TaskBoard
from tools.views import BoostedAbstractView, GenericCreateView


class TODOGenericView(BoostedAbstractView):
    app_name = "todo"


class TODOBaseView(TODOGenericView, TemplateView):
    view_name = "todo_base"
    template_name = "todo_base.html"


class TODOManagementView(TODOGenericView, ListView):
    view_name = "todo_management"
    template_name = "todo_management.html"
    form_class = TODOFilterForm

    def get_filter_form(self, **kwargs):
        return self.form_class(data=self.request.GET or None, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        if not self.filter_form:
            self.filter_form = self.get_filter_form(**self.get_form_kwargs())
        data["filter_form"] = self.filter_form
        data["context"] = self.filter_form.context
        return data

    def get_queryset(self):
        self.filter_form = self.get_filter_form(**self.get_form_kwargs())
        return self.filter_form.get_queryset()

    def get_form_kwargs(self):
        return {"user": self.request.user}


class TODOBoardListView(TODOGenericView, FormView):
    view_name = "board_list"
    template_name = "board_list.html"
    model = TaskBoard
    form_class = TaskBoardHiddenForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_success_url(self) -> str:
        return reverse(self.get_view_name())

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class TaskCreateView(TODOGenericView, GenericCreateView):
    view_name = "task_create"
    form_class = TaskForm
    form_title = "New task"
    back_url = "todo:todo_management"

    def get_success_url(self) -> str:
        return reverse(TODOManagementView.get_view_name() + "?model=Task")


class CategoryCreateView(TODOGenericView, GenericCreateView):
    view_name = "category_create"
    form_class = TaskCategoryForm
    form_title = "New task category"
    back_url = "todo:todo_management"

    def get_success_url(self) -> str:
        return reverse(TODOManagementView.get_view_name() + "?model=Category")
