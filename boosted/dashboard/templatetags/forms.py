from django import template

register = template.Library()


@register.inclusion_tag("filter_form.html")
def filter_form(title: str, form):
    return {"title": title, "form": form}
