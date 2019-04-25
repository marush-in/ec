from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(verbose_name='名前', max_length=250, unique=True)
    slug = models.SlugField(verbose_name='URL', max_length=250, unique=True)
    image = models.ImageField(
        verbose_name='カテゴリー写真',
        upload_to='uploads/',
        max_length=320,
        blank=True
    )
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'

    def __str__(self):
        return self.name

    @property
    def category_image(self):
        return mark_safe(
            '<image src="%s"style="width:100px;height:auto;"/>'
            % self.image.url
        )


class Brand(models.Model):
    name = models.CharField(verbose_name='名前', max_length=250, unique=True)
    slug = models.SlugField(verbose_name='URL', max_length=250, unique=True)
    logo = models.ImageField(
        verbose_name='ロゴ画像', upload_to='uploads/', max_length=320, blank=True
    )
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'ブランド'
        verbose_name_plural = 'ブランド'

    def __str__(self):
        return self.name

    @property
    def brand_image(self):
        return mark_safe(
            '<image src="%s"style="width:100px;height:auto;"/>'
            % self.logo.url
        )


class Product(models.Model):
    name = models.CharField(verbose_name='商品名', max_length=250)
    description = models.TextField(verbose_name='商品説明', max_length=40000)
    slug = models.SlugField(verbose_name='URL', max_length=250, unique=True)
    category = models.ForeignKey(
        Category, verbose_name='カテゴリー', on_delete=models.PROTECT
    )
    brand = models.ForeignKey(
        Brand, verbose_name='ブランド名', on_delete=models.PROTECT
    )
    image = models.ImageField(
        verbose_name='商品写真1', upload_to='uploads/', max_length=320, blank=True
    )
    image2 = models.ImageField(
        verbose_name='商品写真2', upload_to='uploads/', max_length=320, blank=True
    )
    image3 = models.ImageField(
        verbose_name='商品写真3', upload_to='uploads/', max_length=320, blank=True
    )
    price = models.IntegerField(verbose_name='価格', default=1000)
    stock = models.IntegerField(verbose_name='在庫数', default=1)
    is_published = models.BooleanField(verbose_name='公開する', default=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

    def __str__(self):
        return self.name

    @property
    def product_image(self):
        return mark_safe(
            '<image src="%s"style="width:100px;height:auto;"/>'
            % self.image.url
        )


class PopularProduct(models.Model):
    product = models.ForeignKey(
        Product, verbose_name='商品', on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(verbose_name='選択日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = '人気商品'
        verbose_name_plural = '人気商品'

    def __str__(self):
        return self.product.name
