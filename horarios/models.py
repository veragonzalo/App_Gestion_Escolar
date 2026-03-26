from django.db import models
from cursos.models import Curso
from profesores.models import Profesor


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código")
    color = models.CharField(max_length=20, default="blue", verbose_name="Color",
                             help_text="Nombre de color Tailwind: blue, red, green, purple, amber, teal, indigo, rose, etc.")

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class BloqueHorario(models.Model):
    DIAS = [
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
    ]

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='bloques', verbose_name="Curso")
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='bloques', verbose_name="Asignatura")
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name='bloques', verbose_name="Profesor")
    dia_semana = models.IntegerField(choices=DIAS, verbose_name="Día")
    hora_inicio = models.TimeField(verbose_name="Hora inicio")
    hora_fin = models.TimeField(verbose_name="Hora fin")
    sala = models.CharField(max_length=50, blank=True, null=True, verbose_name="Sala")

    class Meta:
        verbose_name = "Bloque Horario"
        verbose_name_plural = "Bloques Horario"
        ordering = ['curso', 'dia_semana', 'hora_inicio']
        unique_together = [['curso', 'dia_semana', 'hora_inicio']]

    def __str__(self):
        return f"{self.curso} | {self.get_dia_semana_display()} {self.hora_inicio:%H:%M} | {self.asignatura}"

    def duracion_minutos(self):
        from datetime import datetime, date
        inicio = datetime.combine(date.today(), self.hora_inicio)
        fin = datetime.combine(date.today(), self.hora_fin)
        return int((fin - inicio).total_seconds() / 60)