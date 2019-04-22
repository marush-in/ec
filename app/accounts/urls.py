from django.urls import path
from .views import login, register, mypage

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('mypage/', mypage, name='mypage'),
]
