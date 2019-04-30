from django.urls import path
from .views import index, confirm

app_name = 'mailmagazine'

urlpatterns = [
    path('', index, name='index'),
    path('confirm/', confirm, name='confirm'),
]
