# Generated by Django 2.1.1 on 2019-04-13 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'カテゴリー', 'verbose_name_plural': 'カテゴリー'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '記事', 'verbose_name_plural': '記事'},
        ),
    ]
