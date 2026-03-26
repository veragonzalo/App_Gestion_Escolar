from django.db import models
from django.contrib.auth.models import User
from profesores.models import Profesor


class PerfilUsuario(models.Model):
    ROL_CHOICES = [
        ('SUPER',      'Superusuario'),
        ('DIRECTOR',   'Director'),
        ('SECRETARIA', 'Administrativo'),
        ('PROFESOR',   'Profesor'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, verbose_name="Rol")
    profesor = models.OneToOneField(
        Profesor, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='perfil_usuario',
        verbose_name="Profesor vinculado",
        help_text="Solo si el rol es Profesor"
    )

    class Meta:
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuario"

    def __str__(self):
        return f"{self.user.username} ({self.get_rol_display()})"

    # Helpers de rol para usar en templates y vistas
    def es_super(self):
        return self.rol == 'SUPER' or self.user.is_superuser

    def es_director(self):
        return self.rol in ('SUPER', 'DIRECTOR') or self.user.is_superuser

    def es_secretaria(self):
        return self.rol in ('SUPER', 'DIRECTOR', 'SECRETARIA') or self.user.is_superuser

    def es_profesor(self):
        return self.rol == 'PROFESOR'

    def puede_editar(self):
        """Puede crear/editar/eliminar registros (no solo ver)"""
        return self.rol in ('SUPER', 'DIRECTOR', 'SECRETARIA') or self.user.is_superuser

    def puede_editar_academico(self):
        """Puede editar notas y asistencia"""
        return self.rol in ('SUPER', 'DIRECTOR', 'PROFESOR') or self.user.is_superuser