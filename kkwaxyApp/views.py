from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .forms import SearchForm
from .models import Post

form  = SearchForm()

class SearchView(TemplateView):
    
    template_name = "kkwaxyApp/search.html"
    http_method_names = ['get', 'post', 'head', 'options', 'trace']

    def post(self, request):
        if(self.request.POST.__contains__("search_terms")):
            search_kwrd = self.request.POST["search_terms"]
            if(search_kwrd == None or search_kwrd == ""):
                pass
            else:
                ctx = self.get_context_data()
                #Search code
                return render(self.request,self.template_name,context=ctx)
        else:
            pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = form
        return context
    
class IndexView(TemplateView):
    
    template_name = "kkwaxyApp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accueil"
        context['latest_posts'] = Post.objects.all()[:5]
        context["search_form"] = form
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

