from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, filters
from rest_framework.filters import OrderingFilter, SearchFilter

from blog.models import Comment, Post
from .paginations import DefaultPagination
from .serializers import CommentSerializer, PostSerializer

# Create your views here.


class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.published.prefetch_related("comments").all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "post"]
    pagination_class = DefaultPagination

    def get_serializer_context(self):
        return {"request": self.request}


class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.prefetch_related("comments").all()

    def get_serializer_context(self):
        return {"request": self.request}


class CommentCreateListView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(post_id=self.kwargs["post_pk"])

    def get_serializer_context(self):
        return {"request": self.request}
