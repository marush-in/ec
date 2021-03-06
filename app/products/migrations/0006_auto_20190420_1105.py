# Generated by Django 2.1.1 on 2019-04-20 02:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190420_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='popularproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='選択日時'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='popularproduct',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
    ]
