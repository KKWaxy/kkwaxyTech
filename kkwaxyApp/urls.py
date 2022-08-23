from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import IndexView,PostDetailView, SearchView
urlpatterns = [
    path("",IndexView.as_view(),name="index"),
    path("post_detail/<int:pk>",PostDetailView.as_view(),name="post_detail"),
    path("search/",SearchView.as_view(),name="search")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
