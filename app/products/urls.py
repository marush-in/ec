from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductListByCategoryView
)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('<slug>/', ProductDetailView.as_view(), name='detail'),
    path(
        'category/<slug>/',
        ProductListByCategoryView.as_view(),
        name='category'
    ),
]
