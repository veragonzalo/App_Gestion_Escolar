from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Asistencia
from .forms import AsistenciaForm
from cursos.models import Curso


@login_required
def portal_asistencia(request):
    total_registros = Asistencia.objects.count()
    presentes = Asistencia.objects.filter(estado='P').count()
    ausentes = Asistencia.objects.filter(estado='A').count()
    justificados = Asistencia.objects.filter(estado='J').count()

    contexto = {
        'total_registros': total_registros,
        'presentes': presentes,
        'ausentes': ausentes,
        'justificados': justificados,
    }
    return render(request, 'asistencia/inicio.html', contexto)


@login_required
def lista_asistencia(request):
    asistencias = Asistencia.objects.select_related('curso', 'alumno').all()

    # Filtros opcionales
    curso_id = request.GET.get('curso')
    fecha = request.GET.get('fecha')

    if curso_id:
        asistencias = asistencias.filter(curso__codigo=curso_id)
    if fecha:
        asistencias = asistencias.filter(fecha=fecha)

    cursos = Curso.objects.all()

    contexto = {
        'asistencias': asistencias,
        'cursos': cursos,
        'filtro_curso': curso_id,
        'filtro_fecha': fecha,
    }
    return render(request, 'asistencia/lista_asistencia.html', contexto)


@login_required
def registrar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia = form.save()
            messages.success(
                request,
                f'Asistencia registrada: {asistencia.alumno} — {asistencia.get_estado_display()}'
            )
            return redirect('lista_asistencia')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = AsistenciaForm()

    contexto = {'form': form}
    return render(request, 'asistencia/registrar_asistencia.html', contexto)


@login_required
def detalle_asistencia(request, asistencia_id):
    asistencia = get_object_or_404(Asistencia, id=asistencia_id)
    contexto = {'asistencia': asistencia}
    return render(request, 'asistencia/detalle_asistencia.html', contexto)


@login_required
def editar_asistencia(request, asistencia_id):
    asistencia = get_object_or_404(Asistencia, id=asistencia_id)

    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asistencia actualizada exitosamente.')
            return redirect('lista_asistencia')
    else:
        form = AsistenciaForm(instance=asistencia)

    contexto = {'form': form, 'asistencia': asistencia}
    return render(request, 'asistencia/editar_asistencia.html', contexto)


@login_required
def eliminar_asistencia(request, asistencia_id):
    asistencia = get_object_or_404(Asistencia, id=asistencia_id)

    if request.method == 'POST':
        asistencia.delete()
        messages.success(request, 'Registro de asistencia eliminado.')
        return redirect('lista_asistencia')

    contexto = {'asistencia': asistencia}
    return render(request, 'asistencia/confirmar_eliminar.html', contexto)
