from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag("button.html")
def button(
    title: str = "Save",
    href: str = None,
    pk: int = None,
    size: str = "sm",
    color: str = "dark-slate-blue",
    extra_classes: str = None,
):
    if href:
        href = reverse(href, kwargs={"pk": pk})
    return {
        "title": title,
        "href": href,
        "size": size,
        "color": color,
        "extra_classes": extra_classes,
    }
