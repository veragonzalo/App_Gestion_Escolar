from django.db import models
from django.contrib.auth.models import User
from cursos.models import Curso


class Comunicado(models.Model):
    TIPO_CHOICES = [
        ('CI', 'Circular'),
        ('AV', 'Aviso'),
        ('UR', 'Urgente'),
    ]
    DESTINATARIOS_CHOICES = [
        ('TO', 'Todos'),
        ('CU', 'Por curso'),
        ('AP', 'Solo apoderados'),
        ('PR', 'Solo profesores'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default='AV', verbose_name="Tipo")
    destinatarios = models.CharField(max_length=2, choices=DESTINATARIOS_CHOICES, default='TO', verbose_name="Destinatarios")
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='comunicados', verbose_name="Curso",
                               help_text="Solo si los destinatarios son 'Por curso'")
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comunicados', verbose_name="Autor")
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Comunicado"
        verbose_name_plural = "Comunicados"
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return f"[{self.get_tipo_display()}] {self.titulo}"

    def color_tipo(self):
        return {'CI': 'blue', 'AV': 'amber', 'UR': 'red'}.get(self.tipo, 'slate')

    def icono_tipo(self):
        return {'CI': 'description', 'AV': 'campaign', 'UR': 'warning'}.get(self.tipo, 'mail')