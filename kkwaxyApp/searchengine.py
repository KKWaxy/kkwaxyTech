from  typing import Union

from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import Post,Tag

def searchByKeyword(keyword: str)-> Union[QuerySet[Post],None]:
    posts = Post.objects.all().filter(title__icontains=keyword)
    if not posts:
        posts = Post.objects.filter(intro__icontains=keyword)
    return posts
    
def searchByTag(tag_name: str) -> Union[QuerySet[Post],None]:
    
    tag_name = tag_name.replace("[","")
    tag_name = tag_name.replace("]","")
    
    try:
        tag = Tag.objects.get(name=tag_name)
    except ObjectDoesNotExist:
        raise Http404("Object does not exsist.")
    
    posts = Post.objects.filter(tags__id=tag.id)
    return posts