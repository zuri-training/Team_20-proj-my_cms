from django.urls import path
from .views import PostCreateView, PostDeleteView, PostUpdateView


urlpatterns = [
# ...
path('post/add/', PostCreateView.as_view(), name='post-add'),
path('post/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
