from django.db import models


# Create your models here.
class Motocykl(models.Model):
    

    KM = models.IntegerField(default=0)
    kolor = models.CharField(max_length=100)
    waga = models.IntegerField(default=0)
    marka = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.marka}'

class Zawody(models.Model):
    Nazwa_toru = models.CharField(max_length=50)
    miejsce= models.CharField(max_length=50)
    Nrtoru = models.IntegerField(default=18)
    poziom_trudnosci = models.IntegerField(default=0)
    pojazd = models.ForeignKey(Motocykl, on_delete=models.CASCADE, blank=True, null=True) #relacja jeden do wielu (klucz obcy)
    def __str__(self):
        return f'{self.Nazwa_toru} {self.miejsce}'

class Kierowca(models.Model):
    doswiadczenie = models.IntegerField(default=0)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    zawody = models.ManyToManyField(Zawody) #relacja wiele do wielu

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'
