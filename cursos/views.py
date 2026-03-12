from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Curso
from .forms import CursoForm


@login_required
def portal_cursos(request):
    # Obtener estadísticas
    total_cursos = Curso.objects.count()
    cursos_activos = total_cursos  # Todos están activos por defecto

    # Contar categorías (puedes personalizar esto según tus necesidades)
    # Por ahora contaremos cuántos cursos únicos hay
    categorias = total_cursos

    contexto = {
        'total_cursos': total_cursos,
        'cursos_activos': cursos_activos,
        'categorias': categorias,
    }

    return render(request, 'cursos/inicio_cursos.html', contexto)


def lista_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "lista_cursos": cursos
    }
    return render(request, 'cursos/lista_cursos.html', contexto)


def nuevo_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            try:
                curso = form.save()
                messages.success(request, f'¡Curso "{curso.nombre}" creado exitosamente!')
                return redirect('lista_cursos')
            except Exception as e:
                messages.error(request, f'Error al guardar: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        form = CursoForm()

    contexto = {
        "form": form
    }
    return render(request, 'cursos/registro_curso.html', contexto)