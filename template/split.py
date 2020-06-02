from django import template

register = template.Library()

@register.filter
def split(stri):
    return stri.split(',')

