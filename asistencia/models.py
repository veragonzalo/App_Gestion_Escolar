from django.db import models
from alumnos.models import Alumno
from cursos.models import Curso


class Asistencia(models.Model):

    ESTADO_CHOICES = [
        ('P', 'Presente'),
        ('A', 'Ausente'),
        ('J', 'Justificado'),
    ]

    fecha = models.DateField(verbose_name="Fecha")
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='asistencias',
        verbose_name="Curso"
    )
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='asistencias',
        verbose_name="Alumno"
    )
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES,
        default='P',
        verbose_name="Estado"
    )
    observacion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observación"
    )

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ['-fecha', 'curso', 'alumno']
        unique_together = [['fecha', 'curso', 'alumno']]

    def __str__(self):
        return f"{self.fecha} | {self.curso} | {self.alumno} | {self.get_estado_display()}"
