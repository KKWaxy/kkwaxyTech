from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import PostListView,IndexView,PostDetailView
urlpatterns = [
    path("",IndexView.as_view(),name="index"),
    path("post_detail/<int:pk>",PostDetailView.as_view(),name="post_detail")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
