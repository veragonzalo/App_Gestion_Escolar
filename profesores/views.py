from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profesor
from .forms import ProfesorForm


@login_required
def portal_profesores(request):

    total_profesores = Profesor.objects.count()
    profesores_activos = total_profesores

    especialidades = Profesor.objects.values_list(
        'profesion',
        flat=True
    ).distinct().count()

    contexto = {
        'total_profesores': total_profesores,
        'profesores_activos': profesores_activos,
        'especialidades': especialidades,
    }

    return render(
        request,
        'profesores/inicio_profesores.html',
        contexto
    )


@login_required
def lista_profesores(request):

    profesores = Profesor.objects.all()

    contexto = {
        "lista_profesores": profesores
    }

    return render(
        request,
        'profesores/lista_profesores.html',
        contexto
    )


@login_required
def nuevo_profesor(request):

    if request.method == "POST":

        form = ProfesorForm(request.POST)

        if form.is_valid():

            try:

                profesor = form.save()

                messages.success(
                    request,
                    f'¡Profesor {profesor.nombre} {profesor.apellido} registrado exitosamente!'
                )

                return redirect('lista_profesores')

            except Exception as e:

                messages.error(
                    request,
                    f'Error al guardar: {str(e)}'
                )

        else:

            messages.error(
                request,
                'Por favor, corrija los errores del formulario.'
            )

    else:

        form = ProfesorForm()

    contexto = {
        "form": form
    }

    return render(
        request,
        'profesores/registro_profesores.html',
        contexto
    )


# -----------------------------
# VER DETALLE PROFESOR
# -----------------------------

@login_required
def detalle_profesor(request, rut):

    profesor = get_object_or_404(
        Profesor,
        rut=rut
    )

    contexto = {
        "profesor": profesor
    }

    return render(
        request,
        'profesores/detalle_profesor.html',
        contexto
    )


# -----------------------------
# EDITAR PROFESOR
# -----------------------------

@login_required
def editar_profesor(request, rut):

    profesor = get_object_or_404(
        Profesor,
        rut=rut
    )

    if request.method == "POST":

        form = ProfesorForm(
            request.POST,
            instance=profesor
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                f'Profesor {profesor.nombre} actualizado correctamente'
            )

            return redirect('lista_profesores')

        else:

            messages.error(
                request,
                'Error al actualizar el profesor'
            )

    else:

        form = ProfesorForm(
            instance=profesor
        )

    contexto = {
        "form": form,
        "profesor": profesor
    }

    return render(
        request,
        'profesores/editar_profesor.html',
        contexto
    )


# -----------------------------
# ELIMINAR PROFESOR
# -----------------------------

@login_required
def eliminar_profesor(request, rut):

    profesor = get_object_or_404(
        Profesor,
        rut=rut
    )

    if request.method == "POST":

        profesor.delete()

        messages.success(
            request,
            f'Profesor {profesor.nombre} eliminado correctamente'
        )

        return redirect('lista_profesores')

    contexto = {
        "profesor": profesor
    }

    return render(
        request,
        'profesores/confirmar_eliminar.html',
        contexto
    )