# Generated by Django 3.2.12 on 2022-04-16 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0002_code2fa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code2fa',
            name='code',
            field=models.IntegerField(default=2614),
        ),
        migrations.AlterField(
            model_name='code2fa',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
