from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post

# Create your views here.

"""
PostListView is going to retrieve all of the objects form the Post table in the db
"""
class PostListView(ListView):
    #template_name attribute is going to be to render a specific html file
    template_name="posts/list.html"
    #model is going to be from which table we want to retrieve the data
    model=Post
    #context is a python dictionary that holds the data for the generic views
    #and this context travels to the htmls
    #by default the context name of ListView and DetailView is "object" or "object_list"
    #context_object_name will allow us to modify that name and how to call it in the htmls
    context_object_name="all_posts"


"""
PostDetailView is going to retrieve a single element from the Post table in the db
"""

class PostDetailView(DetailView):
    template_name="posts/detail.html"
    model=Post
    context_object_name="single_post"


class PostCreateView(CreateView):
    template_name="posts/new.html"
    model=Post
    context_object_name="new_post"
    fields=["title", "subtitle", "body"]