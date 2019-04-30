from django.urls import path
from .views import (
    RegisterMailMagazine,
    RegisterMailMagazineConfirm,
    RegisterMailMagazineComplete,
)

app_name = 'mailmagazine'

urlpatterns = [
    path('', RegisterMailMagazine.as_view(), name='index'),
    path(
        'confirm/',
        RegisterMailMagazineConfirm.as_view(),
        name='register-mailmagazine-confirm'
    ),
    path(
        'complete/<token>',
        RegisterMailMagazineComplete.as_view(),
        name='register-mailmagazine-complete'
    ),
]
