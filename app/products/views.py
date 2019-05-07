from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Product, Category, Brand, Like


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(
        is_published=True).order_by('-created_at')
    paginate_by = 12
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = Product.objects.filter(
            is_published=True).count()
        return context


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
        context['product_count'] = self.get_products_category_count()
        return context

    def get_products_category_count(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(
            category=category, is_published=True
        ).count()


class ProductListByBrandView(ListView):
    model = Product
    paginate_by = 12
    context_object_name = 'products'
    template_name = 'products/products-by-brand.html'

    def get_queryset(self):
        brand = get_object_or_404(Brand, slug=self.kwargs['slug'])
        queryset = Product.objects.filter(
            brand=brand, is_published=True
        ).order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = get_object_or_404(
            Brand, slug=self.kwargs['slug']
        )
        context['brand_count'] = self.get_products_brand_count()
        return context

    def get_products_brand_count(self):
        brand = get_object_or_404(Brand, slug=self.kwargs['slug'])
        return Product.objects.filter(
            brand=brand, is_published=True
        ).count()


def like(request, product_id):
    user = request.user
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        new_like, already_created = Like.objects.get_or_create(
            user=user, product=product
        )
        if already_created:
            return redirect(request.META['HTTP_REFERER'])
        else:
            Like.objects.filter(user=user.id, product=product_id).delete()
            return redirect(request.META['HTTP_REFERER'])
