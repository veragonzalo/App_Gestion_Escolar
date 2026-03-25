from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from alumnos.models import Alumno
from cursos.models import Curso


class Nota(models.Model):

    TIPO_CHOICES = [
        ('PR', 'Prueba'),
        ('TA', 'Tarea'),
        ('EX', 'Examen'),
        ('TR', 'Trabajo'),
        ('PS', 'Presentación'),
        ('OT', 'Otro'),
    ]

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='notas',
        verbose_name="Alumno"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='notas',
        verbose_name="Curso"
    )
    tipo_evaluacion = models.CharField(
        max_length=2,
        choices=TIPO_CHOICES,
        verbose_name="Tipo de Evaluación"
    )
    nota = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(7.0)],
        verbose_name="Nota"
    )
    fecha = models.DateField(verbose_name="Fecha")
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción"
    )

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        ordering = ['-fecha', 'alumno']

    def __str__(self):
        return f"{self.alumno} | {self.curso} | {self.get_tipo_evaluacion_display()} | {self.nota}"

    def aprobado(self):
        return self.nota >= 4.0
