from django.db.models import Q
from django.views.generic import TemplateView

from .models import (
    Guide,
    Privacy_policy,
    Company,
    Terms_of_use,
    Faq,
    Legal,
    Faq_content
)
from products.models import Brand, Category, Product, PopularProduct


class IndevView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_logos'] = Brand.objects.order_by('-created_at')[:6]
        context['categories'] = Category.objects.order_by('-created_at')[:6]
        context['popular_products'] = self.get_popular_products()
        return context

    def get_popular_products(self):
        popular_products = PopularProduct.objects.order_by('-created_at')[:8]
        queries = [
            Q(pk=popular_product.product_id)
            for popular_product in popular_products
        ]
        query = queries.pop()
        for item in queries:
            query |= item
        products = Product.objects.filter(query)
        return products


class GuideView(TemplateView):
    template_name = 'shop/guide.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['giude'] = Guide.objects.first()
        return context


class PrivacyPolicyView(TemplateView):
    template_name = 'shop/privacy_policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['privacy_policy'] = Privacy_policy.objects.first()
        return context


class CompanyView(TemplateView):
    template_name = 'shop/company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.first()
        return context


class TermsOfUseView(TemplateView):
    template_name = 'shop/terms_of_use.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['terms_of_use'] = Terms_of_use.objects.first()
        return context


class FaqView(TemplateView):
    template_name = 'shop/faq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faq_info'] = Faq.objects.first()
        context['faqs'] = Faq_content.objects.all()
        return context


class LegalView(TemplateView):
    template_name = 'shop/legal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['legal'] = Legal.objects.first()
        return context
