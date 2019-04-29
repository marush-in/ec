from django import forms

from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    full_name = forms.CharField(max_length=50)
    name_kana = forms.CharField(max_length=50)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.full_name = self.cleaned_data['full_name']
        user.name_kana = self.cleaned_data['name_kana']
        user.save()
        return user
