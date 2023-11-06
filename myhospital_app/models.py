from django.db import models
from admin_app.models import Departments
from doctor .models import Doctor
from patient.models import Slots




# Create your models here.





    
class Patient(models.Model):
    name = models.CharField(max_length=30)
    age  = models.CharField(max_length=10)
    dob  = models.DateField()
    gender  = models.CharField(max_length=10)
    place  = models.CharField(max_length=30)
    phone  = models.BigIntegerField()
    email  = models.CharField(max_length=30)
    status = models.CharField(max_length=10,default='pending')
    password=models.CharField(max_length=10,default='12345678')
     
    class Meta:
        db_table = 'patient_tb'
        
        
from .models import Patient


class Booking(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=10)   
    gender = models.CharField(max_length=10)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=30)
    department = models.ForeignKey(Departments, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
    slot = models.ForeignKey(Slots,on_delete=models.CASCADE)
    slotTime = models.CharField(max_length=10)
    patient = models.ForeignKey(Patient,null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20,default='pending')
    class Meta:
        db_table = 'booking_tb'
        
class Prescription(models.Model):
    diagnosis = models.CharField(max_length=200)
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    status = models.CharField(max_length=10 , default='active')
    booking = models.ForeignKey(Booking,on_delete = models.CASCADE)
    
    class Meta:
        db_table ='prescription_tb'