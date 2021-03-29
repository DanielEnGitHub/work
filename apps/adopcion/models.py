from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre