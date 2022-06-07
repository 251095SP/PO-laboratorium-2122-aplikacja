from django.shortcuts import render
from django.views import generic
from .models import * 
from .forms import AppForm

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


class ZawodyListView(generic.ListView):
    model = Zawody
    template_name='zawody_index.html'

    def get_queryset(self):
        return Zawody.objects.all()       
        
def form_view(request):
    form = AppForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "forms.html", context)