from django import forms
from datetime import date


class AlumnoForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        max_length=100
    )

    apellido = forms.CharField(
        label='Apellido',
        max_length=100
    )

    edad = forms.IntegerField(
        label='Edad',
        min_value=3,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Ej: 15'
        })
    )

    curso = forms.CharField(
        label='Curso',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: 3° Medio A'
        })
    )

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad:
            if edad < 3:
                raise forms.ValidationError('La edad mínima es 3 años.')
            if edad > 100:
                raise forms.ValidationError('Por favor, ingrese una edad válida.')
        return edad