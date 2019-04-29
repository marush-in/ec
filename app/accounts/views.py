from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import RegisterShippingAddressForm
from .models import ShippingAddress


class ShippingAddressListView(ListView):
    context_object_name = 'shipping_addresses'
    model = ShippingAddress
    template_name = 'accounts/shipping_address_list.html'


class RegisterShippingAddressView(CreateView):
    form_class = RegisterShippingAddressForm
    model = ShippingAddress
    success_url = reverse_lazy('accounts:shipping-address-list')
    template_name = 'accounts/register_shipping_address.html'


@login_required
def mypage(request):
    return render(request, 'accounts/mypage.html')


@login_required
def confirmOrderHistory(request):
    return render(request, 'accounts/confirm_order_history.html')


@login_required
def changeDeliveryInfo(request):
    return render(request, 'accounts/change_delivery_info.html')


@login_required
def changeUserInfo(request):
    return render(request, 'accounts/change_user_info.html')


@login_required
def confirmDeleteUser(request):
    return render(request, 'accounts/confirm_delete_user.html')
