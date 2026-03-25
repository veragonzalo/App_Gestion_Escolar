from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'curso', 'alumno', 'estado']
    list_filter = ['estado', 'fecha', 'curso']
    search_fields = ['alumno__nombre', 'alumno__apellido', 'alumno__rut']
