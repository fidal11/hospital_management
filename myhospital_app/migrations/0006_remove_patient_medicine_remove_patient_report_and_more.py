# Generated by Django 4.2 on 2023-09-21 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhospital_app', '0005_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='report',
        ),
        migrations.AddField(
            model_name='patient',
            name='booking',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myhospital_app.booking'),
        ),
    ]
