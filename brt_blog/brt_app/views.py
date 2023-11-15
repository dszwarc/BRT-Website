from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, CreateView, ListView, DetailView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy
# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    ordering = ['-id']
    model = Post
    template_name = 'home.html'
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')