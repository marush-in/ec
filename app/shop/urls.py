from django.urls import path
from .views import (
    IndevView,
    GuideView,
    PrivacyPolicyView,
    CompanyView,
    TermsOfUseView,
    FaqView,
    LegalView,
    MyView,
)

app_name = 'shop'

urlpatterns = [
    path('', IndevView.as_view(), name='index'),
    path('guide/', GuideView.as_view(), name='guide'),
    path(
        'privacy_policy/', PrivacyPolicyView.as_view(), name='privacy_policy'
    ),
    path('company/', CompanyView.as_view(), name='company'),
    path('terms_of_use/', TermsOfUseView.as_view(), name='terms_of_use'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('legal/', LegalView.as_view(), name='legal'),
    path('myview', MyView.as_view(), name='myview')
]
