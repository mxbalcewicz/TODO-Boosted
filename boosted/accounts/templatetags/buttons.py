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
    onclick: str = None,
    extra_classes: str = None,
    *args,
    **kwargs
):
    if href and pk is not None:
        href = reverse(href, kwargs={"pk": pk})
    elif href:
        href = reverse(href) if href else None
    return {
        "title": title,
        "href": href,
        "size": size,
        "color": color,
        "glyph_class": glyph_class,
        "onclick": onclick,
        "extra_classes": extra_classes,
        "extra_kwargs": kwargs,
    }
