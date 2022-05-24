from django.db import models


# Create your models here.
class Motocykl(models.Model):
    KM = models.IntegerField(default=0)
    kolor = models.CharField(max_length=100)
    waga = models.IntegerField(default=0)
    marka = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.marka}'

class Kierowca(models.Model):
    wiek = models.IntegerField(default=18)
    doswiadczenie = models.IntegerField(default=0)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'
