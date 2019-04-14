from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    confirm_email = forms.EmailField()

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'title',
            'content',
        )
        # exclude = ('created_at',)

        error_messages = {
            'name': {'required': 'お名前が未入力です'},
            'email': {'required': 'メールアドレスが未入力です'},
            'title': {'required': 'お問合せタイトルが未入力です'},
            'content': {'required': 'お問合せ内容が未入力です'},
        }

    def clean(self):
        data = super().clean()
        if data.get('email') != data.get('confirm_email'):
            self.add_error('confirm_email', 'メールアドレスが一致しません。')
        return data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
