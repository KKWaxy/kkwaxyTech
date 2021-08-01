from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Post

class IndexView(TemplateView):
    
    template_name = "kkwaxyApp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accueil" 
        return context
    

class PostListView(ListView):
    model = Post
    template_name = "index.html"

