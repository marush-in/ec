from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    full_name = models.CharField(verbose_name='氏名', max_length=50, blank=True)
    name_kana = models.CharField(
        verbose_name="氏名カナ", max_length=50, blank=True
    )


class ShippingAddress(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(verbose_name='氏名', max_length=50)
    post_code = models.CharField(verbose_name='郵便番号', max_length=7)
    prefecture = models.CharField(verbose_name='都道府県', max_length=10)
    city = models.CharField(verbose_name='市区町村', max_length=100)
    region = models.CharField(verbose_name='町名・番地', max_length=100)
    building_name = models.CharField(
        verbose_name='アパート・マンション名', max_length=50, blank=True
    )
    company_name = models.CharField(
        verbose_name='会社名', max_length=50, blank=True
    )
    phone_number = models.CharField(verbose_name='電話番号', max_length=10)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = '配送住所'
        verbose_name_plural = '配送住所'

    def __str__(self):
        return self.name
