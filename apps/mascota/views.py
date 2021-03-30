from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.form import mascotaForm

from apps.mascota.models import Mascota

# Create your views here.
def index(request):
    return render(request, 'mascota/index.html')

def registroMascota(request):
    if request.method == 'POST':
        form = mascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/mascotas')
    else:
        form = mascotaForm()
    
    return render(request, 'mascota/mascota_form.html', {'form': form})

def listaMascota(request):
    mascota = Mascota.objects.all()
    contexto = {'mascota': mascota}
    return render(request, 'mascota/mascota_list.html', contexto)