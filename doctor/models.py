from django.db import models

from admin_app.models import Departments


import random
# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    age= models.CharField(max_length=30)
    department = models.ForeignKey(Departments, on_delete = models.CASCADE,default=0)
    qualification = models.CharField(max_length=100)
    doctorid = models.CharField(max_length=30)
    password = models.CharField(max_length=30,default='12345678')
    email = models.CharField(max_length=30)
    mobile = models.BigIntegerField(default=1)
    image = models.ImageField(upload_to = 'doctor')
    address = models.CharField(max_length=100,default='')
    status = models.CharField(max_length=10,default='active')
    

    class Meta:
        db_table = 'doctor_tb'
        


