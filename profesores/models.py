from django.db import models

class Profesor(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.rut} {self.nombre} {self.apellido}'

