from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
    path("about", views.about, name="about"),
    path("edit", views.edit, name="edit"),
    path("contact", views.contact, name="contact"),
    path("index", views.index, name="index"),
]
