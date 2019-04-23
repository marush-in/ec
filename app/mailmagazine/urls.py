from django.urls import path
from .views import confirm

app_name = 'mailmagazine'

urlpatterns = [
    path('confirm/', confirm, name='confirm'),
]
