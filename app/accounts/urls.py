from django.urls import path
from .views import (
    mypage,
    CustomUserUpdateView,
    ShippingAddressListView,
    RegisterShippingAddressView,
    UpadateShippingAddressView,
    DeleteShippingAddressView,
    LikeListView,
    confirmOrderHistory,
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
        'likes',
        LikeListView.as_view(),
        name='like-list'
    ),
    path(
        'mypage/confirm-order-history/',
        confirmOrderHistory,
        name='confirm-order-history'
    ),
    path(
        'mypage/confirm-delete-user/',
        confirmDeleteUser,
        name='confirm-delete-user'
    ),
]
