from django import forms, template

register = template.Library()


@register.inclusion_tag("form_field.html")
def form_field(field):
    is_checkbox = (
        True
        if isinstance(
            field.field.widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple)
        )
        else False
    )
    if not is_checkbox:
        field.field.widget.attrs.update({"class": "form-control"})

    return {"field": field, "is_checkbox": is_checkbox}
