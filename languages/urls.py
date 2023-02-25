from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("python/", AboutPageView.as_view(), name="python"),
    path("fsharp/", AboutPageView.as_view(), name="fsharp"),
    path("racket/", AboutPageView.as_view(), name="racket"),
]
