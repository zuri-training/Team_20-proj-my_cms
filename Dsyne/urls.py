"""Dsyne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path, include

# for media handling
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from account import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.registration_view, name='register'),
    path("admin-django/", admin.site.urls),
    # Portfolio url
    path("portfolio/", include("portfolio.urls")),
    # blogPost url
    path("blog/", include("blog.urls")),
    # path for django_cms
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^", include("cms.urls")),
    # url for blog restApi
    path("api/v1/blog/", include("blog.api.urls")),
    # urls for media
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
