from django import forms

from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    full_name = forms.CharField(max_length=50)
    name_kana = forms.CharField(max_length=50)

    def signup(self, request, user):
        user.full_name = self.cleaned_data['full_name']
        user.name_kana = self.cleaned_data['name_kana']
        print(user.full_name)
        user.save()
        return user
