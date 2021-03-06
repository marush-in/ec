# Generated by Django 2.1.1 on 2019-04-23 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190413_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='選択日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post', verbose_name='記事')),
            ],
            options={
                'verbose_name': '人気記事',
                'verbose_name_plural': '人気記事',
            },
        ),
    ]
