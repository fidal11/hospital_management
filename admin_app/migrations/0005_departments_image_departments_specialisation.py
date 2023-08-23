# Generated by Django 4.2 on 2023-08-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_departments'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='image',
            field=models.ImageField(default='', upload_to='departments'),
        ),
        migrations.AddField(
            model_name='departments',
            name='specialisation',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
