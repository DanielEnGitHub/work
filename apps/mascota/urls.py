from django.urls import path

from apps.mascota.views import index, registroMascota, listaMascota

urlpatterns = [
    path('mascotas', index),
    path('registro', registroMascota),
    path('ver', listaMascota),
]
