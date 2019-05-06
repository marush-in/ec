from django.contrib.auth.mixins import LoginRequiredMixin


class AccountsLoginRequiredView(LoginRequiredMixin):
    redirect_field_name = 'accounts/login'
