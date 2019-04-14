from django.db import models


class Contact(models.Model):
    name = models.CharField(verbose_name='お名前', max_length=240)
    email = models.EmailField(verbose_name='メールアドレス', max_length=240)
    title = models.CharField(verbose_name='お問合せタイトル', max_length=240)
    content = models.TextField(verbose_name='お問合せ内容', max_length=4000)

    class Meta:
        verbose_name = 'お問い合わせ内容'
        verbose_name_plural = 'お問い合わせ内容'

    def __str__(self):
        return self.name
