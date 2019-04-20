from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(is_published=True).order_by('-created_at')
    paginate_by = 12
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product


class ProductListByCategoryView(ListView):
    model = Product
    paginate_by = 12
    context_object_name = 'products'
    template_name = 'products/products-by-category.html'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Product.objects.filter(
            category=category, is_published=True
        ).order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category, slug=self.kwargs['slug']
        )
        return context
