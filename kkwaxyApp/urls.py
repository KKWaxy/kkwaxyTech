from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import IndexView,PostDetailView, SearchView
urlpatterns = [
    path("",IndexView.as_view(),name="index"),
    path("post_detail/<int:pk>",PostDetailView.as_view(),name="post_detail"),
    path("search/",SearchView.as_view(),name="search"),
    path("search/<str:tag>", SearchView.as_view(), name="search_tag"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
