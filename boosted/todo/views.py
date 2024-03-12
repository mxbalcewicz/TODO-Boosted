from typing import Any

from django.db.models.query import QuerySet
from django.views.generic import CreateView, ListView, TemplateView
from todo.forms import TaskCategoryForm, TaskForm, TODOFilterForm
from todo.models import Task, TaskBoard, TaskCategory
from tools.views import BoostedAbstractView


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


class TODOBoardListView(TODOGenericView, ListView):
    view_name = "board_list"
    template_name = "board_list.html"
    model = TaskBoard

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.filter()


class TaskCreateView(TODOGenericView, CreateView):
    view_name = "task_create"
    template_name = "task_create.html"
    model = Task
    form_class = TaskForm


class CategoryCreateView(TODOGenericView, CreateView):
    view_name = "category_create"
    template_name = "category_create.html"
    model = TaskCategory
    form_class = TaskCategoryForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    # def get_initial(self) -> dict[str, Any]:
    #     init = super().get_initial()
    #     return init