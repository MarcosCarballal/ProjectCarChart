from django.db import models

# Create your models here.
class Car(models.Model):
    bodyType = models.CharField(max_length=50) #Maybe a choice field?
    emissionsCo2 = models.IntegerField()
    seatingCapacity = models.IntegerField()
    maxSpeed = models.IntegerField()
    fuelCapacity = models.IntegerField()
    price = models.IntegerField()
    manufacturer = models.CharField(max_length = 50)# maybe a choice field?
    model = models.CharField(max_length = 100) 
    enginerPower = models.IntegerField()
