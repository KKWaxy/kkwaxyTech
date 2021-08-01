from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import Post

class IndexView(TemplateView):
    
    template_name = "kkwaxyApp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accueil"
        context['latest_posts'] = Post.objects.all()[:5]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "kkwaxyApp/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "kkwaxyTech/post_detail"
        return context
    


class PostListView(ListView):
    model = Post
    template_name = "index.html"

