from django import template

register = template.Library()

@register.filter
def rangeFun(num):

    return [i for i in range(1,int(num)+1)]