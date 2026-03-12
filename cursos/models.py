from django.db import models
from profesores.models import Profesor
from alumnos.models import Alumno

class Curso(models.Model):
    codigo = models.AutoField(primary_key=True, verbose_name="Código")
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Curso")
    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='cursos',
        verbose_name="Profesor"
    )
    alumnos = models.ManyToManyField(
        Alumno,
        blank=True,
        related_name='cursos',
        verbose_name="Alumnos"
    )

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['nombre']

    def __str__(self):
        return f"[{self.codigo}] {self.nombre}"

    def total_alumnos(self):
        return self.alumnos.count()
