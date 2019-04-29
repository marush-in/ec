from django.urls import path
from .views import (
    mypage,
    CustomUserUpdateView,
    ShippingAddressListView,
    RegisterShippingAddressView,
    UpadateShippingAddressView,
    DeleteShippingAddressView,
    confirmOrderHistory,
    changeDeliveryInfo,
    changeUserInfo,
    confirmDeleteUser,
)

app_name = 'accounts'

urlpatterns = [
    path('mypage/', mypage, name='mypage'),
    path(
        'update-custom-user/<int:pk>',
        CustomUserUpdateView.as_view(),
        name='update-custom-user'
    ),
    path(
        'shipping-address-list',
        ShippingAddressListView.as_view(),
        name='shipping-address-list'
    ),
    path(
        'register-shipping-address',
        RegisterShippingAddressView.as_view(),
        name='register-shipping-address'
    ),
    path(
        'update-shipping-address/<int:pk>',
        UpadateShippingAddressView.as_view(),
        name='update-shipping-address'
    ),
    path(
        'delete-shipping-address/<int:pk>',
        DeleteShippingAddressView.as_view(),
        name='delete-shipping-address'
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
