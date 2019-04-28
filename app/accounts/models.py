from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    full_name = models.CharField(verbose_name='氏名', max_length=50, blank=True)
    name_kana = models.CharField(
        verbose_name="氏名カナ", max_length=50, blank=True
    )
