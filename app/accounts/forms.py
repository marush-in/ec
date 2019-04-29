from django import forms

from allauth.account.forms import SignupForm

from .models import ShippingAddress


class CustomSignupForm(SignupForm):
    full_name = forms.CharField(max_length=50)
    name_kana = forms.CharField(max_length=50)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.full_name = self.cleaned_data['full_name']
        user.name_kana = self.cleaned_data['name_kana']
        user.save()
        return user


class RegisterShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = (
            'name', 'post_code', 'prefecture', 'city', 'region',
            'building_name', 'company_name', 'phone_number'
        )

    # def form_valid(self, form):
    #     self.shipping_adress = form.save(commit=False)
    #     self.shipping_adress.user = self.request.user
    #     self.shipping_adress.save()
    #     return self.shipping_adress
