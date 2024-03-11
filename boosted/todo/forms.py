from enum import Enum

from django import forms
from todo.context_classes import ContextEnum
from todo.models import Task, TaskCategory
from tools.form_tools import update_form_styling


class TODOFilterForm(forms.Form):
    class ModelsChoices(Enum):
        CATEGORY = "Category"
        TASK = "Task"

    model = forms.ChoiceField(
        choices=[(choice.value, choice.value) for choice in ModelsChoices]
    )

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("user")
        super(TODOFilterForm, self).__init__(*args, **kwargs)
        self.context = None
        update_form_styling(self)

    def get_queryset(self):
        queryset = None
        if self.is_valid():
            model_class = self.get_model_class(self.cleaned_data["model"])
            self.context = self.get_context_class(model_class)()
            queryset = model_class.objects.filter(
                **self.context.get_filters(self.request_user)
            )
        return queryset

    def get_model_class(self, choice):
        return {"Category": TaskCategory, "Task": Task}[choice]

    def get_context_class(self, model):
        return ContextEnum.get_class(model)
