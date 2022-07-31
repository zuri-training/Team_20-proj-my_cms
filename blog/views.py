from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)

from .models import Post

""" 
This class lists out all the data in the database that has status equals published and paginates it to multiple pages of 10
"""


class PostListView(ListView):
    model = Post  # this tells that the fields in use is from the Post model
    queryset = (
        Post.published.all()
    )  # return all the queried data that has status as "published"
    paginate_by = 10  # pagination - this separate post into small multiples of 10


""" 
This class create single data point to the  database 
"""


class PostCreateView(CreateView):
    model = Post  # this tells that the fields in use is from the Post model
    queryset = (
        Post.published.all()
    )  # return all the queried data that has status as "published"
    fields = "__all__"  # returns all the fields data


""" 
This class reads single data point in the database 
"""


class PostDetailView(DetailView):
    model = Post  # this tells that the fields in use is from the Post model
    queryset = (
        Post.published.all()
    )  # return all the queried data that has status as "published"
    fields = "__all__"  # returns all the fields data


""" 
This class updates single data point in the database 
"""


class PostUpdateView(UpdateView):
    model = Post  # this tells that the fields in use is from the Post model
    queryset = (
        Post.published.all()
    )  # return all the queried data that has status as "published"
    fields = "__all__"  # returns all the fields data


""" 
This class deletes single data point in the table 
"""


class PostDeleteView(DeleteView):
    model = Post  # this tells that the fields in use is from the Post model
    queryset = (
        Post.published.all()
    )  # return all the queried data that has status as "published"
    fields = "__all__"  # returns all the fields data
