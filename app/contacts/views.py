from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from .forms import ContactForm
from .models import Contact
from shop.models import Settings


class ContactView(CreateView):
    template_name = 'contacts/contact.html'
    form_class = ContactForm
    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recaptacha_public_key'] = settings.RECAPTCHA_PUBLIC_KEY
        print(settings.RECAPTCHA_PUBLIC_KEY)
        return context

    def form_valid(self, form):
        settings = Settings.objects.first()
        data = form.cleaned_data
        send_mail(
            subject='お問い合わせいただきありがとうございます',
            message=render_to_string('mails/contacts/mail_body.txt', {
                'data': data,
            }),
            from_email=settings.mail_from_address,
            recipient_list=[
                form.cleaned_data['email'],
                settings.mail_to_address
            ],
            fail_silently=False,
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contacts:thanks')


class ThanksView(TemplateView):
    template_name = 'contacts/thanks.html'
