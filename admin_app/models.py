from django.db import models

# Create your models here.

class Admin(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = 'admin_tb'
        
        
class Departments(models.Model):
    name = models.CharField(max_length=50)
    specialisation = models.CharField(max_length=30,default='')
    image = models.ImageField(upload_to = 'departments', default='')
    
    class meta:
        db_table = 'departments_tb'