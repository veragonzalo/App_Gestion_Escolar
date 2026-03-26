from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from .models import Asistencia
from cursos.models import Curso
from alumnos.models import Alumno
from usuarios.decorators import requiere_academico


@login_required
def portal_asistencia(request):
    contexto = {
        'total_registros': Asistencia.objects.count(),
        'presentes': Asistencia.objects.filter(estado='P').count(),
        'ausentes': Asistencia.objects.filter(estado='A').count(),
        'justificados': Asistencia.objects.filter(estado='J').count(),
    }
    return render(request, 'asistencia/inicio.html', contexto)


@login_required
def lista_asistencia(request):
    curso_id = request.GET.get('curso', '')
    fecha = request.GET.get('fecha', '')
    asistencias = Asistencia.objects.select_related('curso', 'alumno').all()
    if curso_id:
        asistencias = asistencias.filter(curso__codigo=curso_id)
    if fecha:
        asistencias = asistencias.filter(fecha=fecha)
    contexto = {
        'asistencias': asistencias,
        'cursos': Curso.objects.all(),
        'filtro_curso': curso_id,
        'filtro_fecha': fecha,
        'tiene_filtros': bool(curso_id or fecha),
        'resumen_presentes': asistencias.filter(estado='P').count(),
        'resumen_ausentes': asistencias.filter(estado='A').count(),
        'resumen_justificados': asistencias.filter(estado='J').count(),
    }
    return render(request, 'asistencia/lista_asistencia.html', contexto)


@login_required
def detalle_asistencia(request, asistencia_id):
    asistencia = get_object_or_404(Asistencia, id=asistencia_id)
    return render(request, 'asistencia/detalle_asistencia.html', {'asistencia': asistencia})


@login_required
@requiere_academico
def registrar_asistencia(request):
    cursos = Curso.objects.all()

    if request.method == 'POST':
        curso_codigo = request.POST.get('curso')
        fecha_str = request.POST.get('fecha')
        curso = get_object_or_404(Curso, codigo=curso_codigo)

        try:
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            messages.error(request, 'Fecha inválida.')
            return redirect('registrar_asistencia')

        if fecha_obj > date.today():
            messages.error(request, 'La fecha no puede ser futura.')
            return redirect(f"/asistencia/registrar/?curso={curso_codigo}&fecha={fecha_str}")

        alumnos = curso.alumnos.all()
        if not alumnos.exists():
            messages.warning(request, 'Este curso no tiene alumnos inscritos.')
            return redirect('registrar_asistencia')

        for alumno in alumnos:
            estado = request.POST.get(f'estado_{alumno.rut}', 'A')
            if estado not in ('P', 'A', 'J'):
                estado = 'A'
            Asistencia.objects.update_or_create(
                fecha=fecha_obj,
                curso=curso,
                alumno=alumno,
                defaults={'estado': estado}
            )

        messages.success(request, f'Asistencia guardada: {alumnos.count()} alumnos — {curso.nombre} — {fecha_obj.strftime("%d/%m/%Y")}')
        return redirect('lista_asistencia')

    # GET: cargar alumnos si vienen curso+fecha en query params
    curso_codigo = request.GET.get('curso', '')
    fecha = request.GET.get('fecha', '')
    curso_seleccionado = None
    alumnos_con_estado = []

    if curso_codigo and fecha:
        try:
            curso_seleccionado = Curso.objects.get(codigo=curso_codigo)
            alumnos = curso_seleccionado.alumnos.all().order_by('apellido', 'nombre')
            existentes = {
                a.alumno_id: a.estado
                for a in Asistencia.objects.filter(curso=curso_seleccionado, fecha=fecha)
            }
            alumnos_con_estado = [
                {'alumno': a, 'estado': existentes.get(a.rut, 'P')}
                for a in alumnos
            ]
        except Curso.DoesNotExist:
            pass

    return render(request, 'asistencia/registrar_asistencia.html', {
        'cursos': cursos,
        'curso_seleccionado': curso_seleccionado,
        'alumnos_con_estado': alumnos_con_estado,
        'fecha': fecha,
        'curso_codigo': curso_codigo,
    })


@login_required
@requiere_academico
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
    return render(request, 'asistencia/editar_asistencia.html', {'form': form, 'asistencia': asistencia})


@login_required
@requiere_academico
def eliminar_asistencia(request, asistencia_id):
    asistencia = get_object_or_404(Asistencia, id=asistencia_id)
    if request.method == 'POST':
        asistencia.delete()
        messages.success(request, 'Registro de asistencia eliminado.')
        return redirect('lista_asistencia')
    return render(request, 'asistencia/confirmar_eliminar.html', {'asistencia': asistencia})


@login_required
def resumen_asistencia(request):
    cursos = Curso.objects.all()
    curso_codigo = request.GET.get('curso', '')
    fecha_inicio = request.GET.get('fecha_inicio', '')
    fecha_fin = request.GET.get('fecha_fin', '')
    curso_seleccionado = None
    filas = []
    totales = {'presentes': 0, 'ausentes': 0, 'justificados': 0, 'total': 0}

    if curso_codigo:
        try:
            curso_seleccionado = Curso.objects.get(codigo=curso_codigo)
            alumnos = curso_seleccionado.alumnos.all().order_by('apellido', 'nombre')
            for alumno in alumnos:
                qs = Asistencia.objects.filter(alumno=alumno, curso=curso_seleccionado)
                if fecha_inicio:
                    qs = qs.filter(fecha__gte=fecha_inicio)
                if fecha_fin:
                    qs = qs.filter(fecha__lte=fecha_fin)
                total = qs.count()
                presentes = qs.filter(estado='P').count()
                ausentes = qs.filter(estado='A').count()
                justificados = qs.filter(estado='J').count()
                porcentaje = round((presentes / total) * 100) if total > 0 else None
                filas.append({
                    'alumno': alumno,
                    'total': total,
                    'presentes': presentes,
                    'ausentes': ausentes,
                    'justificados': justificados,
                    'porcentaje': porcentaje,
                })
                totales['presentes'] += presentes
                totales['ausentes'] += ausentes
                totales['justificados'] += justificados
                totales['total'] += total
        except Curso.DoesNotExist:
            pass

    totales['porcentaje'] = round((totales['presentes'] / totales['total']) * 100) if totales['total'] > 0 else None

    return render(request, 'asistencia/resumen.html', {
        'cursos': cursos,
        'curso_seleccionado': curso_seleccionado,
        'curso_codigo': curso_codigo,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'filas': filas,
        'totales': totales,
    })