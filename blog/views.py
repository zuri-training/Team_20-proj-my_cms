from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView,CreateView, DeleteView,UpdateView, DetailView

from .models import Post

class PostListView(ListView):
    model = Post
    queryset = Post.published.all()
    
    

class PostCreateView(CreateView):
    model = Post
    queryset = Post.published.all()
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    queryset = Post.published.all()
    fields = '__all__'
    # success_url = reverse_lazy('blog:all')
    
class PostDeleteView(DeleteView):
    model = Post
    queryset = Post.published.all()
    fields = '__all__'
    # success_url = reverse_lazy('blog:all')
    
    
    