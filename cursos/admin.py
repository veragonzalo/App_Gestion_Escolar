from django.contrib import admin
from . models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

admin.site.register(Curso, CursoAdmin)


# Register your models here.
