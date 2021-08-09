import markdown
from django import template
from django.template.defaultfilters import register, stringfilter
from PIL import Image

register = template.Library()

@register.filter
def convert_markdown(value):
    return markdown.markdown(value,extensions=["markdown.extensions.fenced_code"])

# @register.filter
# def crop_post_media(value):
#     print(value)
#     with Image.open(value) as im:
#         return(im.crop(789.615,))