# from django.conf import settings
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import send_mail
# from django.core.signing import BadSignature, SignatureExpired, loads, dumps
# from django.http import Http404, HttpResponseBadRequest
# from django.shortcuts import render, redirect
# from django.template.loader import render_to_string
# from django.views.generic import CreateView, TemplateView

# from shop.models import Settings
# from .forms import MailMagazineForm
# from .models import MailMagazine


# class RegisterMailMagazine(CreateView):
#     form_class = MailMagazineForm
#     template_name = 'mailmagazine/index.html'

#     def form_valid(self, form):
#         settings_first = Settings.objects.first()
#         data = form.cleaned_data
#         site = get_current_site(self.request)
#         domain = site.domain
#         # context = {
#         #     'protocol': self.request.schema,
#         #     'domain': domain,
#         # }

#         send_mail(
#             subject='[' + settings_first.site_name + ']メールマガジンのご案内',
#             message=render_to_string('mails/mailmagazine/mail_body.txt', {
#                 'data': data,
#                 'site_name': settings_first.site_name
#             }),
#             from_email=settings_first.mail_from_address,
#             recipient_list=[
#                 form.cleaned_data['email'],
#                 settings_first.mail_to_address
#             ],
#             fail_silently=False,
#         )

#         return redirect('mailmagazine:register-mailmagazine-confirm')


# class RegisterMailMagazineConfirm(TemplateView):
#     template_name = 'mailmagazine/register-mailmagazine-confirm.html'


# class RegisterMailMagazineComplete(TemplateView):
#     template_name = 'mailmagazine/register-mailmagazine-complete.html'
#     timeout_seconds = getattr(
#          settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24
#     )

#     def get(self, request, **kwargs):
#         token = kwargs.get('token')
#         try:
#             key = loads(token, max_age=self.timeout_seconds)

#         except SignatureExpired:
#             return HttpResponseBadRequest()
#         except BadSignature:
#             return HttpResponseBadRequest()
