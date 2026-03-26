from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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