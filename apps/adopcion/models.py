from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    domicilio = models.CharField(max_length=10)