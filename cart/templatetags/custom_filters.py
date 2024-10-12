from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """Multiplies the value by the arg."""
    return value * arg
