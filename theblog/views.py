from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView

from theblog.models import Post


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Articles_Details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'Add_Post.html'
    fields = '__all__'


