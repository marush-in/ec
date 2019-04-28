from django.contrib.auth import get_user_model
from django.db import models


class MailMagazine(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True,
    )
    email = models.EmailField(verbose_name='メールアドレス', max_length=254)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'メールマガジン購読者リスト'
        verbose_name_plural = 'メールマガジン購読者リスト'

    def __str__(self):
        return self.email
