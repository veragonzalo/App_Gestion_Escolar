from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profesor
from .forms import ProfesorForm


@login_required
def portal_profesores(request):
    # Obtener estadísticas
    total_profesores = Profesor.objects.count()
    profesores_activos = total_profesores  # Todos están activos por defecto

    # Contar especialidades únicas
    especialidades = Profesor.objects.values_list('profesion', flat=True).distinct().count()

    contexto = {
        'total_profesores': total_profesores,
        'profesores_activos': profesores_activos,
        'especialidades': especialidades,
    }

    return render(request, 'profesores/inicio_profesores.html', contexto)


def lista_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {
        "lista_profesores": profesores
    }
    return render(request, 'profesores/lista_profesores.html', contexto)


def nuevo_profesor(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            try:
                profesor = form.save()
                messages.success(request, f'¡Profesor {profesor.nombre} {profesor.apellido} registrado exitosamente!')
                return redirect('lista_profesores')
            except Exception as e:
                messages.error(request, f'Error al guardar: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        form = ProfesorForm()

    contexto = {
        "form": form
    }
    return render(request, 'profesores/registro_profesores.html', contexto)