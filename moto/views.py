from django.shortcuts import render
from django.views import generic
from .models import * 

 #odpowiedzialna klasa za widoki odnoszące się do wyświetlania listy elementów klasy, w tym przypadku motocykle
class MotoListView(generic.ListView):
    model = Motocykl
    template_name='moto_index.html'

    def get_queryset(self):
        return Motocykl.objects.all()
#odpowiedzialna klasa za widoki odnoszące się do wyświetlania listy elementów klasy, w tym przypadku kierowcy
class KierowcaListView(generic.ListView):
    model = Kierowca
    template_name='kierowca_index.html'

    def get_queryset(self):
        return Kierowca.objects.all()