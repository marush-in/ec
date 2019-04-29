from django.urls import path
from .views import (
    mypage,
    ShippingAddressListView,
    RegisterShippingAddressView,
    confirmOrderHistory,
    changeDeliveryInfo,
    changeUserInfo,
    confirmDeleteUser,
)

app_name = 'accounts'

urlpatterns = [
    path('mypage/', mypage, name='mypage'),
    path(
        'mypage/shipping-address-list',
        ShippingAddressListView.as_view(),
        name='shipping-address-list'
    ),
    path(
        'mypage/register-shipping-address',
        RegisterShippingAddressView.as_view(),
        name='register-shipping-address'
    ),
    path(
        'mypage/confirm-order-history/',
        confirmOrderHistory,
        name='confirm-order-history'
    ),
    path(
        'mypage/change-delivery-info/',
        changeDeliveryInfo,
        name='change-delivery-info'
    ),
    path('mypage/change-user-info/', changeUserInfo, name='change-user-info'),
    path(
        'mypage/confirm-delete-user/',
        confirmDeleteUser,
        name='confirm-delete-user'
    ),
]
