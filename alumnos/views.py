from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Alumno
from .forms import AlumnoForm


@login_required
def portal_alumnos(request):

    total_alumnos = Alumno.objects.count()

    contexto = {
        'total_alumnos': total_alumnos,
        'nuevos_este_mes': 0,
        'cursos_activos': 0,
    }

    return render(request, 'alumnos/inicio.html', contexto)


@login_required
def lista_alumnos(request):

    alumnos = Alumno.objects.all()

    contexto = {
        "lista_alumnos": alumnos
    }

    return render(request, 'alumnos/lista_alumnos.html', contexto)


@login_required
def nuevo_alumno(request):

    if request.method == "POST":

        form = AlumnoForm(request.POST)

        if form.is_valid():

            alumno = form.save()

            messages.success(
                request,
                f'¡Alumno {alumno.nombre} {alumno.apellido} registrado exitosamente!'
            )

            return redirect('lista_alumnos')

        else:

            messages.error(request, 'Por favor corrija los errores del formulario.')

    else:

        form = AlumnoForm()

    contexto = {
        "form": form
    }

    return render(request, 'alumnos/registro_alumno.html', contexto)


@login_required
def detalle_alumno(request, alumno_rut):

    alumno = get_object_or_404(Alumno, rut=alumno_rut)

    contexto = {
        "alumno": alumno
    }

    return render(request, 'alumnos/detalle_alumno.html', contexto)


@login_required
def editar_alumno(request, alumno_rut):

    alumno = get_object_or_404(Alumno, rut=alumno_rut)

    if request.method == "POST":

        form = AlumnoForm(request.POST, instance=alumno)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                f'¡Alumno {alumno.nombre} {alumno.apellido} actualizado exitosamente!'
            )

            return redirect('lista_alumnos')

    else:

        form = AlumnoForm(instance=alumno)

    contexto = {
        "form": form,
        "alumno": alumno
    }

    return render(request, 'alumnos/editar_alumno.html', contexto)


@login_required
def eliminar_alumno(request, alumno_rut):

    alumno = get_object_or_404(Alumno, rut=alumno_rut)

    if request.method == "POST":

        nombre_completo = f"{alumno.nombre} {alumno.apellido}"

        alumno.delete()

        messages.success(
            request,
            f'Alumno {nombre_completo} eliminado exitosamente.'
        )

        return redirect('lista_alumnos')

    contexto = {
        "alumno": alumno
    }

    return render(request, 'alumnos/confirmar_eliminar.html', contexto)