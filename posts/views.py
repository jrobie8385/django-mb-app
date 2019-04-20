from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.

class ViewPosts(ListView):
    model = models.Post
    context_object_name = "posts" #Must put this in quotes.
    template_name = "posts/posts.html"
