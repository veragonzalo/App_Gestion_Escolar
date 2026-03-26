from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Avg
from .models import Alumno
from .forms import AlumnoForm
from usuarios.decorators import requiere_puede_editar
from notas.models import Nota
from asistencia.models import Asistencia


@login_required
def portal_alumnos(request):
    contexto = {
        'total_alumnos': Alumno.objects.count(),
        'nuevos_este_mes': 0,
        'cursos_activos': 0,
    }
    return render(request, 'alumnos/inicio.html', contexto)


@login_required
def lista_alumnos(request):
    q = request.GET.get('q', '').strip()
    alumnos = Alumno.objects.all()
    if q:
        alumnos = alumnos.filter(
            models.Q(nombre__icontains=q) |
            models.Q(apellido__icontains=q) |
            models.Q(rut__icontains=q)
        )
    paginator = Paginator(alumnos, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'alumnos/lista_alumnos.html', {"page_obj": page_obj, "q": q})


@login_required
def detalle_alumno(request, alumno_rut):
    alumno = get_object_or_404(Alumno, rut=alumno_rut)
    return render(request, 'alumnos/detalle_alumno.html', {"alumno": alumno})


@login_required
@requiere_puede_editar
def nuevo_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save()
            messages.success(request, f'Alumno {alumno.nombre} {alumno.apellido} registrado exitosamente.')
            return redirect('lista_alumnos')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/registro_alumno.html', {"form": form})


@login_required
@requiere_puede_editar
def editar_alumno(request, alumno_rut):
    alumno = get_object_or_404(Alumno, rut=alumno_rut)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            messages.success(request, f'Alumno {alumno.nombre} {alumno.apellido} actualizado exitosamente.')
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/editar_alumno.html', {"form": form, "alumno": alumno})


@login_required
def perfil_alumno(request, alumno_rut):
    alumno = get_object_or_404(Alumno, rut=alumno_rut)

    notas_por_curso = []
    for curso in alumno.cursos.all():
        notas = Nota.objects.filter(alumno=alumno, curso=curso).order_by('-fecha')
        promedio = notas.aggregate(Avg('nota'))['nota__avg']
        notas_por_curso.append({
            'curso': curso,
            'notas': notas,
            'promedio': round(float(promedio), 1) if promedio else None,
        })

    asistencia_por_curso = []
    total_asistencias = 0
    total_presentes = 0
    for curso in alumno.cursos.all():
        qs = Asistencia.objects.filter(alumno=alumno, curso=curso)
        total = qs.count()
        presentes = qs.filter(estado='P').count()
        ausentes = qs.filter(estado='A').count()
        justificados = qs.filter(estado='J').count()
        porcentaje = round((presentes / total) * 100) if total > 0 else None
        asistencia_por_curso.append({
            'curso': curso,
            'total': total,
            'presentes': presentes,
            'ausentes': ausentes,
            'justificados': justificados,
            'porcentaje': porcentaje,
        })
        total_asistencias += total
        total_presentes += presentes

    porcentaje_global = round((total_presentes / total_asistencias) * 100) if total_asistencias > 0 else 0

    return render(request, 'alumnos/perfil_alumno.html', {
        'alumno': alumno,
        'notas_por_curso': notas_por_curso,
        'asistencia_por_curso': asistencia_por_curso,
        'total_asistencias': total_asistencias,
        'porcentaje_asistencia': porcentaje_global,
        'apoderados': alumno.apoderados.all(),
    })


@login_required
@requiere_puede_editar
def eliminar_alumno(request, alumno_rut):
    alumno = get_object_or_404(Alumno, rut=alumno_rut)
    if request.method == "POST":
        nombre_completo = f"{alumno.nombre} {alumno.apellido}"
        alumno.delete()
        messages.success(request, f'Alumno {nombre_completo} eliminado exitosamente.')
        return redirect('lista_alumnos')
    return render(request, 'alumnos/confirmar_eliminar.html', {"alumno": alumno})