from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from alumnos.models import Alumno
from profesores.models import Profesor
from cursos.models import Curso
from notas.models import Nota
from asistencia.models import Asistencia
from apoderados.models import Apoderado


def inicio(request):
    contexto = {
        'total_alumnos': Alumno.objects.count(),
        'total_profesores': Profesor.objects.count(),
        'total_cursos': Curso.objects.count(),
        'total_notas': Nota.objects.count(),
        'total_asistencias': Asistencia.objects.count(),
        'total_apoderados': Apoderado.objects.count(),
    }
    return render(request, "base.html", contexto)



