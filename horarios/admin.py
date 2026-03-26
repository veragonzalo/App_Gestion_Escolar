from django.contrib import admin
from .models import Asignatura, BloqueHorario

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo', 'color']
    search_fields = ['nombre', 'codigo']

@admin.register(BloqueHorario)
class BloqueHorarioAdmin(admin.ModelAdmin):
    list_display = ['curso', 'dia_semana', 'hora_inicio', 'hora_fin', 'asignatura', 'profesor', 'sala']
    list_filter = ['dia_semana', 'curso', 'asignatura']