from django.shortcuts import render
# List query sets and view in detail retrieved db info
from django.views.generic import ListView, DetailView
from .models import Post


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'