# Generated by Django 4.2 on 2023-09-14 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=100)),
                ('staffid', models.CharField(max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.BigIntegerField()),
                ('image', models.ImageField(upload_to='staff')),
            ],
            options={
                'db_table': 'staff_tb',
            },
        ),
    ]
