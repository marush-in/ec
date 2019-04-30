from django import forms

from .models import MailMagazine


class MailMagazineForm(forms.ModelForm):
    class Meta:
        model = MailMagazine
        fields = ('email',)
