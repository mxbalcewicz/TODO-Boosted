from django import template

register = template.Library()


@register.inclusion_tag("form_input_field.html")
def form_input_field(field):
    field.field.widget.attrs.update({"class": "form-control"})
    return {"field": field}


@register.inclusion_tag("form_checkbox_field.html")
def form_checkbox_field(field):
    return {"field": field}


@register.inclusion_tag("file_input.html")
def form_file_input_field(field, accepted_types=None):
    field.field.widget.attrs.update({"class": "form-control"})
    return {"field": field, "accepted_types": accepted_types}
