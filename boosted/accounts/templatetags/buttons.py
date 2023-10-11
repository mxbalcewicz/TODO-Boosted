from django import template

register = template.Library()


@register.inclusion_tag("button.html")
def button(title: str = "", href: str = "#", size="lg", color="primary"):
    return {"title": title, "href": href, "size": size, "color": color}
