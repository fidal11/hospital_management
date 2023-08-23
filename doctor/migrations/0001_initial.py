# Generated by Django 4.2 on 2023-08-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=100)),
                ('doctorid', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='doctor')),
            ],
            options={
                'db_table': 'doctor_tb',
            },
        ),
    ]
