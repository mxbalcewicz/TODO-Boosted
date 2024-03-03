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
    glyph_class: str = None,
    extra_classes: str = None,
):
    if pk is not None:
        href = reverse(href, kwargs={"pk": pk})
    else:
        href = reverse(href) if href else None
    return {
        "title": title,
        "href": href,
        "size": size,
        "color": color,
        "glyph_class": glyph_class,
        "extra_classes": extra_classes,
    }
