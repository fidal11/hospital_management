from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=30)
    age= models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    staffid = models.CharField(max_length=30)
    password = models.CharField(max_length=30,default='')
    email = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    image = models.ImageField(upload_to = 'staff')
    

    class Meta:
        db_table = 'staff_tb'