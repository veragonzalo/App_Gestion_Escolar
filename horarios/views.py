from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Asignatura, BloqueHorario
from .forms import AsignaturaForm, BloqueHorarioForm
from cursos.models import Curso


DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']


@login_required
def inicio_horarios(request):
    contexto = {
        'total_asignaturas': Asignatura.objects.count(),
        'total_bloques': BloqueHorario.objects.count(),
        'total_cursos': Curso.objects.count(),
        'cursos': Curso.objects.all(),
        'asignaturas': Asignatura.objects.all(),
    }
    return render(request, 'horarios/inicio.html', contexto)


# ── ASIGNATURAS ────────────────────────────────────────────

@login_required
def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'horarios/lista_asignaturas.html', {'asignaturas': asignaturas})


@login_required
def crear_asignatura(request):
    form = AsignaturaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_asignaturas')
    return render(request, 'horarios/form_asignatura.html', {'form': form, 'titulo': 'Nueva Asignatura'})


@login_required
def detalle_asignatura(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    bloques = asignatura.bloques.select_related('curso', 'profesor').order_by('dia_semana', 'hora_inicio')
    return render(request, 'horarios/detalle_asignatura.html', {'asignatura': asignatura, 'bloques': bloques})


@login_required
def editar_asignatura(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    form = AsignaturaForm(request.POST or None, instance=asignatura)
    if form.is_valid():
        form.save()
        return redirect('detalle_asignatura', pk=pk)
    return render(request, 'horarios/form_asignatura.html', {'form': form, 'titulo': 'Editar Asignatura', 'asignatura': asignatura})


@login_required
def eliminar_asignatura(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('lista_asignaturas')
    return render(request, 'horarios/confirmar_eliminar_asignatura.html', {'asignatura': asignatura})


# ── BLOQUES HORARIO ────────────────────────────────────────

@login_required
def lista_bloques(request):
    curso_id = request.GET.get('curso')
    bloques = BloqueHorario.objects.select_related('curso', 'asignatura', 'profesor')
    if curso_id:
        bloques = bloques.filter(curso_id=curso_id)
    cursos = Curso.objects.all()
    return render(request, 'horarios/lista_bloques.html', {
        'bloques': bloques.order_by('dia_semana', 'hora_inicio'),
        'cursos': cursos,
        'curso_seleccionado': curso_id,
    })


@login_required
def crear_bloque(request):
    form = BloqueHorarioForm(request.POST or None)
    curso_inicial = request.GET.get('curso')
    if curso_inicial:
        form.fields['curso'].initial = curso_inicial
    if form.is_valid():
        bloque = form.save()
        return redirect('horario_curso', curso_pk=bloque.curso.pk)
    return render(request, 'horarios/form_bloque.html', {'form': form, 'titulo': 'Agregar Bloque'})


@login_required
def editar_bloque(request, pk):
    bloque = get_object_or_404(BloqueHorario, pk=pk)
    form = BloqueHorarioForm(request.POST or None, instance=bloque)
    if form.is_valid():
        bloque = form.save()
        return redirect('horario_curso', curso_pk=bloque.curso.pk)
    return render(request, 'horarios/form_bloque.html', {'form': form, 'titulo': 'Editar Bloque', 'bloque': bloque})


@login_required
def eliminar_bloque(request, pk):
    bloque = get_object_or_404(BloqueHorario, pk=pk)
    if request.method == 'POST':
        curso_pk = bloque.curso.pk
        bloque.delete()
        return redirect('horario_curso', curso_pk=curso_pk)
    return render(request, 'horarios/confirmar_eliminar_bloque.html', {'bloque': bloque})


# ── HORARIO SEMANAL DE UN CURSO ────────────────────────────

@login_required
def horario_curso(request, curso_pk):
    curso = get_object_or_404(Curso, pk=curso_pk)
    bloques = BloqueHorario.objects.filter(curso=curso).select_related('asignatura', 'profesor').order_by('dia_semana', 'hora_inicio')

    # Organizar bloques como lista de (nombre_dia, [bloques]) para el template
    por_dia = {i: [] for i in range(5)}
    for bloque in bloques:
        por_dia[bloque.dia_semana].append(bloque)

    horario_semana = [(DIAS[i], por_dia[i]) for i in range(5)]

    cursos = Curso.objects.all()
    return render(request, 'horarios/horario_curso.html', {
        'curso': curso,
        'horario_semana': horario_semana,
        'cursos': cursos,
        'tiene_bloques': any(por_dia[i] for i in range(5)),
    })