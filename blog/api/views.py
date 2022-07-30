from django.shortcuts import render
from rest_framework import status, generics

from .serializers import CommentSerializer, PostSerializer
from .models import Comment, Post

# Create your views here.

class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    
    def get_serializer_context(self):
        return {"request": self.request}
    


class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()
  
    
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