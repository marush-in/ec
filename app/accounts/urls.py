from django.urls import path
from .views import (
    login,
    register,
    mypage,
    confirmOrderHistory,
    changeDeliveryInfo,
    changeUserInfo,
    confirmDeleteUser,
)

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('mypage/', mypage, name='mypage'),
    path('mypage/confirm-order-history/', confirmOrderHistory, name='confirm-order-history'),
    path('mypage/change-delivery-info/', changeDeliveryInfo, name='change-delivery-info'),
    path('mypage/change-user-info/', changeUserInfo, name='change-user-info'),
    path('mypage/confirm-delete-user/', confirmDeleteUser, name='confirm-delete-user'),
]
