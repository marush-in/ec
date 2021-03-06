# Generated by Django 2.1.1 on 2019-04-20 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product', verbose_name='商品')),
            ],
            options={
                'verbose_name': '人気商品',
                'verbose_name_plural': '人気商品',
            },
        ),
    ]
