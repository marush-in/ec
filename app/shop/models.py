from django.db import models


class Settings(models.Model):
    site_name = models.CharField(verbose_name='サイト名', max_length=160)
    site_description = models.TextField(verbose_name='サイトの説明', max_length=240)
    mail_from_address = models.EmailField(
        verbose_name='メール送信元',
        max_length=254,
        default='fromexample@marushin.mn'
    )
    mail_to_address = models.EmailField(
        verbose_name='メール送信先', max_length=254, default='toexample@marushin.mn'
    )
    ogp_iamge = models.ImageField(
        verbose_name='OGP画像', upload_to='uploads/', max_length=320, blank=True
    )
    ga_tag = models.TextField(
        verbose_name='GoogleAnalyticsタグ', max_length=600, blank=True
    )
    instagram = models.CharField(
        verbose_name='Instagram', max_length=240, blank=True
    )
    facebook = models.CharField(
        verbose_name='Facebook', max_length=240, blank=True
    )
    twitter = models.CharField(
        verbose_name='Twitter', max_length=240, blank=True
    )
    youtube = models.CharField(
        verbose_name='Youtube', max_length=240, blank=True
    )
    line = models.CharField(verbose_name='Line', max_length=240, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'サイト基本情報'
        verbose_name_plural = 'サイト基本情報'

    def __str__(self):
        return self.site_name


class Guide(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=160)
    description = models.TextField(verbose_name='ディスクリプション', max_length=240)
    content = models.TextField(verbose_name='本文', max_length=40000)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'ご利用ガイド'
        verbose_name_plural = 'ご利用ガイド'

    def __str__(self):
        return self.title


class Privacy_policy(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=160)
    description = models.TextField(verbose_name='ディスクリプション', max_length=240)
    content = models.TextField(verbose_name='本文', max_length=40000)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'プライバシーポリシー'
        verbose_name_plural = 'プライバシーポリシー'

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=160)
    description = models.TextField(verbose_name='ディスクリプション', max_length=240)
    content = models.TextField(verbose_name='本文', max_length=40000)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = '運営会社'
        verbose_name_plural = '運営会社'

    def __str__(self):
        return self.title


class Terms_of_use(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=160)
    description = models.TextField(verbose_name='ディスクリプション', max_length=240)
    content = models.TextField(verbose_name='本文', max_length=40000)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'ご利用規約'
        verbose_name_plural = 'ご利用規約'

    def __str__(self):
        return self.title


class Faq(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=160)
    description = models.TextField(verbose_name='ディスクリプション', max_length=240)
    content = models.TextField(verbose_name='本文', max_length=40000)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'よくあるお問い合わせ'
        verbose_name_plural = 'よくあるお問い合わせ'

    def __str__(self):
        return self.title


class Legal(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=160)
    description = models.TextField(verbose_name='ディスクリプション', max_length=240)
    content = models.TextField(verbose_name='本文', max_length=40000)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = '特定商取引法に基づく表記'
        verbose_name_plural = '特定商取引法に基づく表記'

    def __str__(self):
        return self.title


class Faq_content(models.Model):
    question = models.CharField(verbose_name='質問', max_length=2000)
    answer = models.TextField(verbose_name='答え', max_length=2000)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'よくあるお問い合わせの項目'
        verbose_name_plural = 'よくあるお問い合わせの項目'

    def __str__(self):
        return self.question
