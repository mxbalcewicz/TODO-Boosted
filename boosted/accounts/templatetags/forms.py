from django import template

register = template.Library()


@register.inclusion_tag("form_field.html")
def form_field(field):
    field.field.widget.attrs.update({"class": "form-control"})
    return {"field": field}
