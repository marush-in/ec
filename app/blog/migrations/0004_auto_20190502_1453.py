# Generated by Django 2.1.1 on 2019-05-02 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_popularpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='eyecatch',
            new_name='origin',
        ),
    ]
