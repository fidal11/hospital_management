from django.db import models
from admin_app.models import Departments
from doctor .models import Doctor


# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=30)
    age  = models.CharField(max_length=10)
    dob  = models.DateField()
    gender  = models.CharField(max_length=10)
    place  = models.CharField(max_length=30)
    phone  = models.BigIntegerField()
    email  = models.CharField(max_length=30)
    department = models.ForeignKey(Departments, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
    date_of_appoinment = models.DateField()
    report = models.CharField(max_length=100,default='none')
    medicine = models.CharField(max_length=100,default='none')
    status = models.CharField(max_length=10,default='pending')
    password=models.CharField(max_length=10,default='')
    class Meta:
        db_table = 'patient_tb'

    
    
    
    
    
    
