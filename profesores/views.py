from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms


@login_required
def portal_profesores(request):
    return render(request, 'profesores/inicio_profesores.html')


def lista_profesores(request):
    profesores = ["Juan Mayorga", "Omar Monsalve", "Felix Cañoles", "Sergio Perez", "Leticia Ojeda"]
    contexto = {
        "lista_profesores": profesores
    }
    return render(request, 'profesores/lista_profesores.html', contexto)


def nuevo_profesor(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            profesion = form.cleaned_data['profesion']

            # Aquí deberías guardar en la base de datos
            # Profesor.objects.create(
            #     rut=rut,
            #     nombre=nombre,
            #     apellido=apellido,
            #     fecha_nacimiento=fecha_nacimiento,
            #     profesion=profesion
            # )

            contexto_post = {
                "rut": rut,
                "nombre": nombre,
                "apellido": apellido,
                "fecha_nacimiento": fecha_nacimiento,
                "profesion": profesion,
            }

            # Agregar mensaje de éxito
            messages.success(request, f'¡Profesor {nombre} {apellido} registrado exitosamente!')

            return render(request, 'profesores/registro_exito.html', contexto_post)
        else:
            # Agregar mensaje de error si el formulario no es válido
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        form = forms.ProfesorForm()

    contexto = {
        "form": form
    }
    return render(request, 'profesores/registro_profesores.html', contexto)