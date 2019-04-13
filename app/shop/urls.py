from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('guide/', views.guide, name='guide'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('company/', views.privacy_policy, name='company'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('faq/', views.faq, name='faq'),
    path('legal/', views.legal, name='legal'),
]