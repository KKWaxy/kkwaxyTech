import kkwaxyTech.settings
from django.conf.urls.static import static
from django.urls import path

from .views import PostListView,IndexView
urlpatterns = [
    path("",IndexView.as_view(),name="index")
] + static(kkwaxyTech.settings.MEDIA_URL)
