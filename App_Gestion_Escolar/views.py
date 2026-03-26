from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from alumnos.models import Alumno
from profesores.models import Profesor
from cursos.models import Curso
from notas.models import Nota
from asistencia.models import Asistencia
from apoderados.models import Apoderado
from comunicaciones.models import Comunicado


@login_required
def inicio(request):
    contexto = {
        'total_alumnos': Alumno.objects.count(),
        'total_profesores': Profesor.objects.count(),
        'total_cursos': Curso.objects.count(),
        'total_notas': Nota.objects.count(),
        'total_asistencias': Asistencia.objects.count(),
        'total_apoderados': Apoderado.objects.count(),
        'comunicados_recientes': Comunicado.objects.filter(activo=True)[:4],
    }
    return render(request, "inicio.html", contexto)


@login_required
def buscar_global(request):
    q = request.GET.get('q', '').strip()
    alumnos = profesores = cursos = []
    if len(q) >= 2:
        alumnos = Alumno.objects.filter(
            Q(nombre__icontains=q) | Q(apellido__icontains=q) | Q(rut__icontains=q)
        )[:15]
        profesores = Profesor.objects.filter(
            Q(nombre__icontains=q) | Q(apellido__icontains=q) | Q(rut__icontains=q)
        )[:15]
        cursos = Curso.objects.filter(
            Q(nombre__icontains=q)
        )[:10]
    total = len(alumnos) + len(profesores) + len(cursos)
    return render(request, 'buscar.html', {
        'q': q, 'alumnos': alumnos, 'profesores': profesores,
        'cursos': cursos, 'total': total,
    })



