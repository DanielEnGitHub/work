from django.urls import path

from apps.adopcion.views import index

urlpatterns = [
    path('index', index),
]
