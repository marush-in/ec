from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView, TemplateView
)

from .forms import RegisterShippingAddressForm, CustomUserUpdateForm
from .models import CustomUser, ShippingAddress
from products.models import Product, Like


class CustomUserUpdateView(LoginRequiredMixin, UpdateView):
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


class CustomUserDeleteView(LoginRequiredMixin, DeleteView):
    context_object_name = 'user'
    model = get_user_model()
    success_url = reverse_lazy('accounts:delete-done-costom-user')
    template_name = 'accounts/delete_costom_user.html'


class CustomUserDeleteDoneView(TemplateView):
    template_name = 'accounts/delete_done_costom_user.html'


class ShippingAddressListView(LoginRequiredMixin, ListView):
    context_object_name = 'shipping_addresses'
    model = ShippingAddress
    template_name = 'accounts/shipping_address_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = ShippingAddress.objects.filter(user_id=user.id)
        return queryset


class RegisterShippingAddressView(LoginRequiredMixin, CreateView):
    form_class = RegisterShippingAddressForm
    model = ShippingAddress
    success_url = reverse_lazy('accounts:shipping-address-list')
    success_url = reverse_lazy('accounts:shipping-address-list')
    template_name = 'accounts/register_shipping_address.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(RegisterShippingAddressView, self).form_valid(form)


class UpadateShippingAddressView(LoginRequiredMixin, UpdateView):
    form_class = RegisterShippingAddressForm
    model = ShippingAddress
    success_url = reverse_lazy('accounts:shipping-address-list')
    template_name = 'accounts/register_shipping_address.html'


class DeleteShippingAddressView(LoginRequiredMixin, DeleteView):
    context_object_name = 'shipping_address'
    model = ShippingAddress
    success_url = reverse_lazy('accounts:shipping-address-list')
    template_name = 'accounts/delete_shipping_address.html'


class LikeListView(LoginRequiredMixin, ListView):
    context_object_name = 'products'
    model = Like
    paginate_by = 12
    template_name = 'accounts/like_list.html'

    def get_queryset(self):
        user = self.request.user
        likes = Like.objects.filter(user=user)
        if likes:
            queries = [Q(pk=like.product_id) for like in likes]
            query = queries.pop()
            for item in queries:
                query |= item
            queryset = Product.objects.filter(query)
            return queryset
        return


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
