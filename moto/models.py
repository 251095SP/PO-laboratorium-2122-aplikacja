from django.db import models


# Create your models here.
class Motocykl(models.Model):
    KM = models.IntegerField(default=0)
    kolor = models.CharField(max_length=100)
    waga = models.IntegerField(default=0)
    marka = models.CharField(max_length=100)
