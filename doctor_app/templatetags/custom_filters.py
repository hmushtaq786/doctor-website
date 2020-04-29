from django import template
import datetime

register = template.Library()


@register.filter(name='day')
def day(value):
    return value.strftime("%d")


@register.filter(name='month')
def month(value):
    return value.strftime("%b")


@register.filter(name='year')
def year(value):
    return value.strftime("%Y")
