# Generated by Django 3.2 on 2022-05-05 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0005_auto_20220504_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='residents.own'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='changed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='closed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='code2fa',
            name='code',
            field=models.IntegerField(),
        ),
    ]