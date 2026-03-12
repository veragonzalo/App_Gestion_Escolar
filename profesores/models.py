from django.db import models

class Profesor(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name="RUT")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    profesion = models.CharField(max_length=150, verbose_name="Profesión")

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"
