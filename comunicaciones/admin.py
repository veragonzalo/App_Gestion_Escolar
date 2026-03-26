from django.contrib import admin
from .models import Comunicado


@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'destinatarios', 'autor', 'fecha_publicacion', 'activo']
    list_filter = ['tipo', 'destinatarios', 'activo']
    search_fields = ['titulo', 'contenido']