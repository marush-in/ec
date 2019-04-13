from django.views.generic import TemplateView


class IndevView(TemplateView):
    template_name = 'shop/index.html'


class GuideView(TemplateView):
    template_name = 'shop/guide.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'shop/privacy_policy.html'


class CompanyView(TemplateView):
    template_name = 'shop/company.html'


class TermsOfUseView(TemplateView):
    template_name = 'shop/terms_of_use.html'


class FaqView(TemplateView):
    template_name = 'shop/faq.html'


class Legal(TemplateView):
    template_name = 'shop/legal.html'
