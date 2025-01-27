from django.utils.formats import number_format
from django import template

register = template.Library()

@register.filter
def replace_space(value):
    return value.replace(" ", "-")

@register.filter
def format_number(value):
    if value >= 1_000_000:
        return f'{value // 1_000_000}m'
    elif value >= 1_000:
        return f'{value // 1_000}k'
    return value

@register.filter
def format_amount(value):
    return f'₦{value:,.0f}'
