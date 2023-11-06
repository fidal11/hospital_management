from django.db import models
from doctor .models import Doctor

# Create your models here.


class Slots(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    status = models.CharField(max_length=20,default='available')
    
    class Meta:
        db_table = 'slots_tb'