from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Category


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=True).order_by('-created_at')
    paginate_by = 12
    context_object_name = 'posts'
    template_name = 'blog/index.html'


class PostDetailView(DetailView):
    model = Post


class PostListByCategoryView(ListView):
    model = Post
    paginate_by = 12
    context_object_name = 'posts'
    template_name = 'blog/posts-by-category.html'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Post.objects.filter(
            category=category, is_published=True
        ).order_by('-created_at')
        return queryset
