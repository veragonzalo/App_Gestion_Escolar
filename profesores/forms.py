from django import forms

class ProfesorForm(forms.Form):
    nombre_profesor = forms.CharField(label='Nombre: ', max_length=100)
    apellido_profesor = forms.CharField(label='Apellido: ', max_length=100)
    edad_profesor = forms.CharField(label='Edad: ', max_length=100)
    curso_profesor = forms.CharField(label='Curso: ', max_length=100)