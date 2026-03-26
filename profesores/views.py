from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profesor
from .forms import ProfesorForm
from usuarios.decorators import requiere_puede_editar


@login_required
def portal_profesores(request):
    contexto = {
        'total_profesores': Profesor.objects.count(),
        'profesores_activos': Profesor.objects.count(),
        'especialidades': Profesor.objects.values_list('profesion', flat=True).distinct().count(),
    }
    return render(request, 'profesores/inicio_profesores.html', contexto)


@login_required
def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores/lista_profesores.html', {"lista_profesores": profesores})


@login_required
def detalle_profesor(request, rut):
    profesor = get_object_or_404(Profesor, rut=rut)
    return render(request, 'profesores/detalle_profesor.html', {"profesor": profesor})


@login_required
@requiere_puede_editar
def nuevo_profesor(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            try:
                profesor = form.save()
                messages.success(request, f'Profesor {profesor.nombre} {profesor.apellido} registrado exitosamente.')
                return redirect('lista_profesores')
            except Exception as e:
                messages.error(request, f'Error al guardar: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        form = ProfesorForm()
    return render(request, 'profesores/registro_profesores.html', {"form": form})


@login_required
@requiere_puede_editar
def editar_profesor(request, rut):
    profesor = get_object_or_404(Profesor, rut=rut)
    if request.method == "POST":
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profesor {profesor.nombre} actualizado correctamente.')
            return redirect('lista_profesores')
        else:
            messages.error(request, 'Error al actualizar el profesor.')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'profesores/editar_profesor.html', {"form": form, "profesor": profesor})


@login_required
@requiere_puede_editar
def eliminar_profesor(request, rut):
    profesor = get_object_or_404(Profesor, rut=rut)
    if request.method == "POST":
        profesor.delete()
        messages.success(request, f'Profesor {profesor.nombre} eliminado correctamente.')
        return redirect('lista_profesores')
    return render(request, 'profesores/confirmar_eliminar.html', {"profesor": profesor})