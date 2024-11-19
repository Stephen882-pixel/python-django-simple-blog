from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView

from theblog.models import Post
from . forms import PostForm,EditForm


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Articles_Details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Add_Post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'Update_Post.html'
    form_class = EditForm
    #fields = ['title', 'title_tag','body']



