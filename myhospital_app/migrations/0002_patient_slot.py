# Generated by Django 4.2 on 2023-09-17 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        ('myhospital_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='slot',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='patient.slots'),
        ),
    ]