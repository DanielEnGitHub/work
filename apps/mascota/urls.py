from django.urls import path

from apps.mascota.views import index, registroMascota

urlpatterns = [
    path('mascotas', index),
    path('registro', registroMascota),
]
