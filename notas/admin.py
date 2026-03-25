from django.contrib import admin
from .models import Nota

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'alumno', 'curso', 'tipo_evaluacion', 'nota']
    list_filter = ['tipo_evaluacion', 'fecha', 'curso']
    search_fields = ['alumno__nombre', 'alumno__apellido', 'alumno__rut']
