from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, PopularPost, Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=True).order_by('-created_at')
    paginate_by = 8
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_posts'] = self.get_popular_posts()
        return context

    def get_popular_posts(self):
        popular_posts = PopularPost.objects.order_by('-created_at')[:5]
        queries = [
            Q(pk=popular_post.post_id)
            for popular_post in popular_posts
        ]
        query = queries.pop()
        for item in queries:
            query |= item
        posts = Post.objects.filter(query)
        return posts


class PostListByCategoryView(ListView):
    model = Post
    paginate_by = 8
    context_object_name = 'posts'
    template_name = 'blog/posts-by-category.html'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Post.objects.filter(
            category=category, is_published=True
        ).order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category, slug=self.kwargs['slug']
        )
        return context
