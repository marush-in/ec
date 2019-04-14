from django.urls import path
from .views import (
    ContactView,
    ThanksView
)

app_name = 'contacts'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/thanks', ThanksView.as_view(), name='thanks'),
]
