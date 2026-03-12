from django import forms
from datetime import date
from .models import Profesor


class ProfesorForm(forms.ModelForm):
    """Formulario basado en el modelo Profesor"""

    # Sobrescribir el campo fecha_nacimiento para controlar el formato
    fecha_nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={
            'type': 'date',  # Usar input type="date" HTML5
            'class': 'form-control'
        }),
        input_formats=['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y'],  # Aceptar múltiples formatos
    )

    class Meta:
        model = Profesor
        fields = ['rut', 'nombre', 'apellido', 'fecha_nacimiento', 'profesion']
        widgets = {
            'rut': forms.TextInput(attrs={
                'placeholder': '12.345.678-9',
                'class': 'form-control'
            }),
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre',
                'class': 'form-control'
            }),
            'apellido': forms.TextInput(attrs={
                'placeholder': 'Ingrese el apellido',
                'class': 'form-control'
            }),
            'profesion': forms.TextInput(attrs={
                'placeholder': 'Ej: Profesor de Matemáticas',
                'class': 'form-control'
            }),
        }

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha:
            # Validar que la fecha no sea futura
            if fecha > date.today():
                raise forms.ValidationError('La fecha de nacimiento no puede ser futura.')

            # Validar edad mínima (18 años)
            edad = (date.today() - fecha).days // 365
            if edad < 18:
                raise forms.ValidationError('El profesor debe tener al menos 18 años.')

        return fecha

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if rut:
            rut = rut.strip()
            if len(rut) < 9:
                raise forms.ValidationError('Ingrese un RUT válido.')
        return rut