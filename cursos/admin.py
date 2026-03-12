from django.contrib import admin
from .models import Curso


class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'profesor', 'total_alumnos')
    search_fields = ('codigo', 'nombre', 'profesor__nombre', 'profesor__apellido')
    list_filter = ('profesor',)
    filter_horizontal = ('alumnos',)
    ordering = ('nombre',)

    def total_alumnos(self, obj):
        return obj.total_alumnos()
    total_alumnos.short_description = 'Total Alumnos'


admin.site.register(Curso, CursoAdmin)
