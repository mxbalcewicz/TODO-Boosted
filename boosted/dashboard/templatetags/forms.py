from django import template

register = template.Library()


@register.inclusion_tag("filter_form.html")
def filter_form(title: str, form):
    return {"title": title, "form": form}


@register.inclusion_tag("generic_form.html")
def generic_form(title: str, form, id: str = None):
    return {"title": title, "form": form, "id": id}
