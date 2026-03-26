from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg
from .models import Nota
from .forms import NotaForm
from cursos.models import Curso
from alumnos.models import Alumno
from usuarios.decorators import requiere_academico


@login_required
def portal_notas(request):
    total_notas = Nota.objects.count()
    promedio = Nota.objects.aggregate(promedio=Avg('nota'))['promedio']
    contexto = {
        'total_notas': total_notas,
        'promedio': round(promedio, 1) if promedio else 0,
        'aprobadas': Nota.objects.filter(nota__gte=4.0).count(),
        'reprobadas': Nota.objects.filter(nota__lt=4.0).count(),
    }
    return render(request, 'notas/inicio.html', contexto)


@login_required
def lista_notas(request):
    notas = Nota.objects.select_related('alumno', 'curso').all()
    curso_id = request.GET.get('curso')
    alumno_rut = request.GET.get('alumno')
    if curso_id:
        notas = notas.filter(curso__codigo=curso_id)
    if alumno_rut:
        notas = notas.filter(alumno__rut=alumno_rut)
    contexto = {
        'notas': notas,
        'cursos': Curso.objects.all(),
        'alumnos': Alumno.objects.all(),
        'filtro_curso': curso_id,
        'filtro_alumno': alumno_rut,
    }
    paginator = Paginator(notas, 20)
    page_obj = paginator.get_page(request.GET.get('page'))
    contexto['page_obj'] = page_obj
    contexto.pop('notas')
    return render(request, 'notas/lista_notas.html', contexto)


@login_required
def detalle_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    return render(request, 'notas/detalle_nota.html', {'nota': nota})


@login_required
@requiere_academico
def registrar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save()
            messages.success(request, f'Nota {nota.nota} registrada para {nota.alumno} en {nota.curso}.')
            return redirect('lista_notas')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = NotaForm()
    return render(request, 'notas/registrar_nota.html', {'form': form})


@login_required
@requiere_academico
def editar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota actualizada exitosamente.')
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/editar_nota.html', {'form': form, 'nota': nota})


@login_required
@requiere_academico
def eliminar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    if request.method == 'POST':
        nota.delete()
        messages.success(request, 'Nota eliminada exitosamente.')
        return redirect('lista_notas')
    return render(request, 'notas/confirmar_eliminar.html', {'nota': nota})


@login_required
def boletin_notas(request):
    cursos = Curso.objects.all()
    curso_codigo = request.GET.get('curso', '')
    curso_seleccionado = None
    filas = []
    promedio_curso = None
    total_aprobados = 0

    if curso_codigo:
        try:
            curso_seleccionado = Curso.objects.get(codigo=curso_codigo)
            alumnos = curso_seleccionado.alumnos.all().order_by('apellido', 'nombre')

            for alumno in alumnos:
                notas = Nota.objects.filter(alumno=alumno, curso=curso_seleccionado)
                total_notas = notas.count()
                avg = notas.aggregate(Avg('nota'))['nota__avg']
                promedio = round(float(avg), 1) if avg else None

                # Promedios por tipo
                tipos_data = {}
                for codigo, label in Nota.TIPO_CHOICES:
                    notas_tipo = notas.filter(tipo_evaluacion=codigo)
                    if notas_tipo.exists():
                        avg_tipo = notas_tipo.aggregate(Avg('nota'))['nota__avg']
                        tipos_data[codigo] = {
                            'label': label,
                            'promedio': round(float(avg_tipo), 1),
                            'count': notas_tipo.count(),
                        }

                if promedio and promedio >= 4.0:
                    total_aprobados += 1

                # Build ordered list for template iteration
                tipos_list = []
                for codigo, label in Nota.TIPO_CHOICES:
                    tipos_list.append(tipos_data.get(codigo))

                filas.append({
                    'alumno': alumno,
                    'total_notas': total_notas,
                    'promedio': promedio,
                    'tipos_list': tipos_list,
                    'aprobado': promedio >= 4.0 if promedio else None,
                })

            if filas:
                promedios_validos = [f['promedio'] for f in filas if f['promedio']]
                if promedios_validos:
                    promedio_curso = round(sum(promedios_validos) / len(promedios_validos), 1)

        except Curso.DoesNotExist:
            pass

    return render(request, 'notas/boletin.html', {
        'cursos': cursos,
        'curso_seleccionado': curso_seleccionado,
        'curso_codigo': curso_codigo,
        'filas': filas,
        'promedio_curso': promedio_curso,
        'total_aprobados': total_aprobados,
        'total_reprobados': len(filas) - total_aprobados,
        'tipo_choices': Nota.TIPO_CHOICES,
    })