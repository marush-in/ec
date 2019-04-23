from django.urls import path
from .views import thanks

app_name = 'orders'

urlpatterns = [
    path('thanks/', thanks, name='thanks'),
]
