from django.db import models
from alumnos.models import Alumno


class Apoderado(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name="RUT")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo Electrónico")
    direccion = models.CharField(max_length=200, blank=True, null=True, verbose_name="Dirección")
    alumnos = models.ManyToManyField(
        Alumno,
        blank=True,
        related_name='apoderados',
        verbose_name="Alumnos a cargo"
    )

    class Meta:
        verbose_name = "Apoderado"
        verbose_name_plural = "Apoderados"
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"
