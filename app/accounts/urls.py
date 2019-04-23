from django.urls import path
from .views import login, register, mypage, confirmOrderHistory

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('mypage/', mypage, name='mypage'),
    path('mypage/confirm-order-history/', confirmOrderHistory, name='confirm-order-history'),
]
