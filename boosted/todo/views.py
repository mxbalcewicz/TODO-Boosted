from django.urls import reverse
from django.views.generic import DeleteView, FormView, ListView, TemplateView
from todo.forms import (
    TaskBoardForm,
    TaskBoardHiddenForm,
    TaskCategoryForm,
    TaskForm,
    TODOFilterForm,
)
from todo.models import Task, TaskBoard, TaskCategory
from tools.views import (
    BoostedAbstractView,
    GenericCreateView,
    GenericDetailView,
    GenericQueryParamsMixin,
)


class TODOGenericView(BoostedAbstractView):
    app_name = "todo"


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


class TODOBoardListView(TODOGenericView, FormView):
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


class TaskCreateView(TODOGenericView, GenericCreateView):
    view_name = "task_create"
    form_class = TaskForm
    form_title = "New task"
    list_url = "todo:todo_management"

    def get_success_url(self):
        return reverse(TODOManagementView.get_view_name() + "?model=Task")


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


class CategoryCreateView(TODOGenericView, GenericCreateView):
    view_name = "category_create"
    form_class = TaskCategoryForm
    form_title = "New task category"
    list_url = "todo:todo_management"

    def get_success_url(self):
        return reverse(TODOManagementView.get_view_name() + "?model=Category")


class CategoryDetailView(
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


class TaskDeleteView(TODOGenericView, DeleteView):
    view_name = "task_delete"
    model = Task

    def get_success_url(self) -> str:
        return reverse(TODOManagementView.get_view_name()) + "?model=Task"


class TaskCategoryDeleteView(TODOGenericView, DeleteView):
    view_name = "category_delete"
    model = TaskCategory

    def get_success_url(self) -> str:
        return reverse(TODOManagementView.get_view_name()) + "?model=Category"
