from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.form import mascotaForm

# Create your views here.
def index(request):
    return render(request, 'mascota/index.html')

def registroMascota(request):
    if request.method == 'POST':
        form = mascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/zmascotas')
    else:
        form = mascotaForm()
    
    return render(request, 'mascota/mascota_form.html', {'form': form})