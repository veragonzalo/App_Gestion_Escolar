from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Curso
from .forms import CursoForm
from alumnos.models import Alumno
from usuarios.decorators import requiere_puede_editar


@login_required
def portal_cursos(request):
    contexto = {
        'total_cursos': Curso.objects.count(),
        'cursos_activos': Curso.objects.count(),
        'categorias': Curso.objects.count(),
    }
    return render(request, 'cursos/inicio_cursos.html', contexto)


@login_required
def lista_cursos(request):
    q = request.GET.get('q', '').strip()
    cursos = Curso.objects.all()
    if q:
        cursos = cursos.filter(
            Q(nombre__icontains=q) | Q(codigo__icontains=q)
        )
    paginator = Paginator(cursos, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'cursos/lista_cursos.html', {"page_obj": page_obj, "q": q})


@login_required
def detalle_curso(request, codigo):
    curso = get_object_or_404(Curso, codigo=codigo)
    return render(request, 'cursos/detalle_curso.html', {'curso': curso})


@login_required
@requiere_puede_editar
def nuevo_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            try:
                curso = form.save()
                messages.success(request, f'Curso "{curso.nombre}" creado exitosamente.')
                return redirect('lista_cursos')
            except Exception as e:
                messages.error(request, f'Error al guardar: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        form = CursoForm()
    return render(request, 'cursos/registro_curso.html', {"form": form})


@login_required
@requiere_puede_editar
def editar_curso(request, codigo):
    curso = get_object_or_404(Curso, codigo=codigo)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('detalle_curso', codigo=codigo)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form, 'curso': curso})


@login_required
@requiere_puede_editar
def eliminar_curso(request, codigo):
    curso = get_object_or_404(Curso, codigo=codigo)
    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')
    return render(request, 'cursos/confirmar_eliminar.html', {'curso': curso})


@login_required
@requiere_puede_editar
def matricular_alumnos(request, codigo):
    curso = get_object_or_404(Curso, codigo=codigo)
    q = request.GET.get('q', '').strip()
    todos_alumnos = Alumno.objects.all().order_by('apellido', 'nombre')
    if q:
        todos_alumnos = todos_alumnos.filter(
            Q(nombre__icontains=q) | Q(apellido__icontains=q) | Q(rut__icontains=q)
        )
    inscritos_ids = set(curso.alumnos.values_list('rut', flat=True))

    if request.method == 'POST':
        seleccionados = request.POST.getlist('alumnos')
        curso.alumnos.set(seleccionados)
        messages.success(request, f'{len(seleccionados)} alumno(s) matriculado(s) en {curso.nombre}.')
        return redirect('detalle_curso', codigo=codigo)

    return render(request, 'cursos/matricular.html', {
        'curso': curso,
        'todos_alumnos': todos_alumnos,
        'inscritos_ids': inscritos_ids,
        'q': q,
    })