from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def portal_alumnos(request):
    return render(request, 'alumnos/inicio.html')

def lista_alumnos(request):
    alumnos = ["Gonzalo Vera", "Pedro Guzman", "Luis Torres", "Maria Barria"]
    contexto = {
        "lista_alumnos": alumnos
    }
    return render(request, 'alumnos/lista_alumnos.html', contexto)


def nuevo_alumno(request):
    if request.method == "GET":
        form = forms.AlumnoForm()
    else:
        form = forms.AlumnoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            edad = form.cleaned_data['edad']
            curso = form.cleaned_data['curso']

            contexto_post = {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "curso": curso,
            }

            # aca se deberian tomar las variables y guardarlas en la base de datos
            # enviar mensaje de confirmacion " nuevo alumno ingresado exitosamente"
            return render(request, 'alumnos/registro_exito.html', contexto_post)
    contexto = {
        "form": form
    }
    return render(request,'alumnos/registro_alumno.html', contexto)



