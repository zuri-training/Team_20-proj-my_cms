from django.urls import path

from .views import (
    PostCreateListView,
    PostRetrieveUpdateDeleteView,
    CommentCreateListView,
    CommentRetrieveUpdateDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("post/", PostCreateListView.as_view()),
    path("post/<int:pk>/", PostRetrieveUpdateDeleteView.as_view()),
    path("comment/", CommentCreateListView.as_view()),
    path("comment/<int:pk>/", CommentRetrieveUpdateDeleteView.as_view()),
]
