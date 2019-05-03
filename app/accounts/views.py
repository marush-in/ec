from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .forms import RegisterShippingAddressForm, CustomUserUpdateForm
from .models import CustomUser, ShippingAddress


class CustomUserUpdateView(UpdateView):
    form_class = CustomUserUpdateForm
    model = get_user_model()
    template_name = 'accounts/update_costom_user.html'

    def get_queryset(self):
        user = self.request.user
        queryset = CustomUser.objects.filter(id=user.id)
        return queryset

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('accounts:update-custom-user', kwargs={
            'pk': pk}
        )


class ShippingAddressListView(ListView):
    context_object_name = 'shipping_addresses'
    model = ShippingAddress
    template_name = 'accounts/shipping_address_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = ShippingAddress.objects.filter(user_id=user.id)
        return queryset


class RegisterShippingAddressView(CreateView):
    form_class = RegisterShippingAddressForm
    model = ShippingAddress
    success_url = reverse_lazy('accounts:shipping-address-list')
    success_url = reverse_lazy('accounts:shipping-address-list')
    template_name = 'accounts/register_shipping_address.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(RegisterShippingAddressView, self).form_valid(form)


class UpadateShippingAddressView(UpdateView):
    form_class = RegisterShippingAddressForm
    model = ShippingAddress
    success_url = reverse_lazy('accounts:shipping-address-list')
    template_name = 'accounts/register_shipping_address.html'


class DeleteShippingAddressView(DeleteView):
    context_object_name = 'shipping_address'
    model = ShippingAddress
    success_url = reverse_lazy('accounts:shipping-address-list')
    template_name = 'accounts/delete_shipping_address.html'


@login_required
def mypage(request):
    user = request.user
    return render(request, 'accounts/mypage.html', {
        'user': user
    })


@login_required
def confirmOrderHistory(request):
    return render(request, 'accounts/confirm_order_history.html')


@login_required
def confirmDeleteUser(request):
    return render(request, 'accounts/confirm_delete_user.html')
