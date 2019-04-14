from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from .forms import ContactForm
from .models import Contact


class ContactView(CreateView):
    template_name = 'contacts/contact.html'
    form_class = ContactForm
    model = Contact

    def get_success_url(self):
        return reverse('contacts:thanks')


class ThanksView(TemplateView):
    template_name = 'contacts/thanks.html'
