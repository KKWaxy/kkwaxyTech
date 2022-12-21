from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.http import Http404

from .forms import SearchForm
from .models import Post,Tag
from .searchengine import searchByKeyword,searchByTag

form  = SearchForm()
tags = Tag.objects.all()

class BaseView(TemplateView):
    pass

class SearchView(TemplateView):
    
    template_name = "kkwaxyApp/search.html"
    http_method_names = ['get', 'post', 'head', 'options', 'trace']

    def post(self, request):
        ctx = self.get_context_data()
        if(request.POST.__contains__("search_terms")):
            search_kwrd = request.POST["search_terms"]
            if(search_kwrd != None and search_kwrd != ""):
                if(str(search_kwrd).startswith('[') and str(search_kwrd).endswith(']')):
                    ctx["posts"]= searchByTag(search_kwrd)
                else: 
                    ctx["posts"] = searchByKeyword(search_kwrd)
        return render(request,self.template_name,context=ctx)
    
    def get(self, request, tag=None):
        if not tag:
            raise Http404("Tag can't be empty.")
        ctx = self.get_context_data()
        ctx['posts'] = searchByTag(tag)
        return render(request,template_name=self.template_name, context=ctx)
    
    def search(self, word):
        pass
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = form
        context["tags"] = tags[:5]
        return context
        
class IndexView(TemplateView):
    
    template_name = "kkwaxyApp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accueil"
        context['posts'] = Post.objects.all()[:5]
        context["search_form"] = form
        context["tags"] = tags
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "kkwaxyApp/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "kkwaxyTech/post_detail"
        context["search_form"] = form
        context["tags"] = tags[:5]
        return context

    