# Generated by Django 2.1.1 on 2019-04-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_terms_of_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=240, verbose_name='ディスクリプション'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='description',
            field=models.TextField(max_length=240, verbose_name='ディスクリプション'),
        ),
        migrations.AlterField(
            model_name='faq_content',
            name='answer',
            field=models.TextField(max_length=2000, verbose_name='答え'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='description',
            field=models.TextField(max_length=240, verbose_name='ディスクリプション'),
        ),
        migrations.AlterField(
            model_name='legal',
            name='description',
            field=models.TextField(max_length=240, verbose_name='ディスクリプション'),
        ),
        migrations.AlterField(
            model_name='privacy_policy',
            name='description',
            field=models.TextField(max_length=240, verbose_name='ディスクリプション'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='ga_tag',
            field=models.TextField(blank=True, max_length=600, verbose_name='GoogleAnalyticsタグ'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='site_description',
            field=models.TextField(max_length=240, verbose_name='サイトの説明'),
        ),
        migrations.AlterField(
            model_name='terms_of_use',
            name='description',
            field=models.TextField(max_length=240, verbose_name='ディスクリプション'),
        ),
    ]
