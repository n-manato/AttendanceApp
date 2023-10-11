from django import template

register = template.Library()

@register.filter
def get_by_index(iterable, index):
    try:
        return iterable[index]
    except (IndexError, KeyError, TypeError):
        return None
