from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'contacts/contact.html'


class ThanksView(TemplateView):
    template_name = 'contacts/thanks.html'
