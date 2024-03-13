from django import template

register = template.Library()


@register.inclusion_tag("filter_form.html")
def filter_form(title: str, form):
    return {"title": title, "form": form}


@register.inclusion_tag("generic_form.html")
def generic_form(title: str, form, back_url: str):
    return {"title": title, "form": form, "back_url": back_url}
