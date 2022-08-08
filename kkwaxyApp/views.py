from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView

from .forms import SearchForm
from .models import Post

form  = SearchForm()

class SearchView(TemplateView):
    
    template_name = "kkwaxyApp/search.html"
    http_method_names = ['get', 'post', 'head', 'options', 'trace']

    def post(self, request):
        ctx = self.get_context_data()
        if(request.POST.__contains__("search_terms")):
            search_kwrd = request.POST["search_terms"]
            if(search_kwrd != None and search_kwrd != ""):
                posts = Post.objects.all().filter(title__icontains=search_kwrd)
            ctx["posts"] = posts
        return render(request,self.template_name,context=ctx)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = form
        return context
    
class IndexView(TemplateView):
    
    template_name = "kkwaxyApp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accueil"
        context['posts'] = Post.objects.all()[:5]
        context["search_form"] = form
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "kkwaxyApp/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "kkwaxyTech/post_detail"
        context["search_form"] = form
        return context

class PostListView(ListView):
    model = Post
    template_name = "index.html"

class CreatePostView(CreateView):
    model = Post
    fields = ['title','intro','body','media']
    template_name_suffix = '_create_form.html'
    