# Generated by Django 4.2 on 2023-09-21 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhospital_app', '0003_patient_slottime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='department',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='slot',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='slotTime',
        ),
    ]
