from django import template
from menu.tree_menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag("tree_menu/menu_tag.html", takes_context=True)
def draw_menu(context, menu_name, parent_id=None, url=None):
    request = context['request']
    items = MenuItem.objects.filter(menu__name=menu_name, parent=parent_id).select_related("parent")
    return {"items": items, 'request': request}
    