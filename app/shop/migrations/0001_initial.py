# Generated by Django 2.1.1 on 2019-04-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='タイトル')),
                ('description', models.CharField(max_length=240, verbose_name='ディスクリプション')),
                ('content', models.TextField(max_length=40000, verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': '運営会社',
                'verbose_name_plural': '運営会社',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='タイトル')),
                ('description', models.CharField(max_length=240, verbose_name='ディスクリプション')),
                ('content', models.TextField(max_length=40000, verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': 'よくあるお問い合わせ',
                'verbose_name_plural': 'よくあるお問い合わせ',
            },
        ),
        migrations.CreateModel(
            name='Faq_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2000, verbose_name='質問')),
                ('answer', models.CharField(max_length=2000, verbose_name='答え')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': 'よくあるお問い合わせの項目',
                'verbose_name_plural': 'よくあるお問い合わせの項目',
            },
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='タイトル')),
                ('description', models.CharField(max_length=240, verbose_name='ディスクリプション')),
                ('content', models.TextField(max_length=40000, verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': 'ご利用ガイド',
                'verbose_name_plural': 'ご利用ガイド',
            },
        ),
        migrations.CreateModel(
            name='Legal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='タイトル')),
                ('description', models.CharField(max_length=240, verbose_name='ディスクリプション')),
                ('content', models.TextField(max_length=40000, verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': '特定商取引法に基づく表記',
                'verbose_name_plural': '特定商取引法に基づく表記',
            },
        ),
        migrations.CreateModel(
            name='Privacy_policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='タイトル')),
                ('description', models.CharField(max_length=240, verbose_name='ディスクリプション')),
                ('content', models.TextField(max_length=40000, verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': 'プライバシーポリシー',
                'verbose_name_plural': 'プライバシーポリシー',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=160, verbose_name='サイト名')),
                ('site_description', models.CharField(max_length=240, verbose_name='サイトの説明')),
                ('ogp_iamge', models.ImageField(blank=True, max_length=320, upload_to='uploads/', verbose_name='OGP画像')),
                ('ga_tag', models.CharField(blank=True, max_length=600, verbose_name='GoogleAnalyticsタグ')),
                ('instagram', models.CharField(blank=True, max_length=240, verbose_name='Instagram')),
                ('facebook', models.CharField(blank=True, max_length=240, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=240, verbose_name='Twitter')),
                ('youtube', models.CharField(blank=True, max_length=240, verbose_name='Youtube')),
                ('line', models.CharField(blank=True, max_length=240, verbose_name='Line')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': 'ご利用ガイド',
                'verbose_name_plural': 'ご利用ガイド',
            },
        ),
    ]