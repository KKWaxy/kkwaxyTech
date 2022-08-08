import markdown
from django import template
from django.template.defaultfilters import register

register = template.Library()

@register.filter
def convert_markdown(value):
    return markdown.markdown(value,extensions=["markdown.extensions.fenced_code"])

@register.filter
def intro_wrap(value):
    value = str(value)[0:250]+"..."
    return value