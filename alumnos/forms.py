from django import forms

# Esta clase solo sirve para renderizar los formularios HTML
class AlumnoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    correo_electronico = forms.EmailField(label='Correo electronico')

