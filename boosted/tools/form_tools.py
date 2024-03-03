from django.forms import BaseForm
from django import forms

def update_form_styling(form: BaseForm):
    for field_name, field in form.fields.items():
        if isinstance(field.widget, forms.CheckboxInput):
            continue
        form.fields[field_name].widget.attrs.update({"class": "form-control"})
        if isinstance(field, forms.ModelMultipleChoiceField):
            form.fields[field_name].widget.attrs.update({"class": "form-control chosen"})
