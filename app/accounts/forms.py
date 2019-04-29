from django import forms
# from django.contrib.auth import get_user_model

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


# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('full_name', 'name_kana')


class RegisterShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = (
            'name', 'post_code', 'prefecture', 'city', 'region',
            'building_name', 'company_name', 'phone_number'
        )
