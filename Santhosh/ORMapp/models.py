from django.db import models
from django.contrib import admin
# Create your models here.
class Car(models.Model):
    car_name=models.CharField(max_length=20)
    car_no=models.CharField(primary_key=True,max_length=10)
    buyer=models.CharField(max_length=20)
    date_of_purchase=models.DateTimeField()
    Address=models.CharField(max_length=100)

class CarAdmin(admin.ModelAdmin):
    list_display=['car_name','car_no','buyer','date_of_purchase','Address']