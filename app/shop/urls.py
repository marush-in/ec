from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('guide/', views.guide, name='guide'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy')
]