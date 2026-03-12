from django.db import models

class Alumno(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name="RUT")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"
