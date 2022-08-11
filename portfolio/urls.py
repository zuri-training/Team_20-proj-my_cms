from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
    path("about", views.about, name="about"),
]
