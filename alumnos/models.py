from django.db import models

# las clases aca creadas seusan para crear la BD:
#1. Aca se crean clases python
#2. Se leeran y creara un plano para migrarlas a  la BD


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


