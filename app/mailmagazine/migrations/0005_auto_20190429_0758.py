# Generated by Django 2.1.1 on 2019-04-28 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailmagazine', '0004_mailmagazine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailmagazine',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
