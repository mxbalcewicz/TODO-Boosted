from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag("bento_box.html")
def bento_box(
    title: str = "",
    href: str = "#",
    colsize: int = 4,
    extra_classes: str = None,
    form=None,
    glyph_class: str = None,
    reverse_url=False,
):
    if reverse_url:
        href = reverse(href)
    return {
        "title": title,
        "href": href,
        "glyph_class": glyph_class,
        "colsize": colsize,
        "extra_classes": extra_classes,
        "form": form,
    }
