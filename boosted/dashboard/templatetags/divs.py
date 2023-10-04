from django import template

register = template.Library()


@register.inclusion_tag("bento_box.html")
def bento_box(title: str = "", href: str = "#", colsize: int = 4):
    return {"title": title, "href": href, "colsize": colsize}
