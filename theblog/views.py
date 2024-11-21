from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from theblog.models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Articles_Details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Add_Post.html'  # fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'Update_Post.html'
    form_class = EditForm  # fields = ['title', 'title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'Add_Category.html'
    fields = '__all__'


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-',' '), 'category_posts': category_posts})

