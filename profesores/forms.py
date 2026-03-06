from django import forms
from datetime import date


class ProfesorForm(forms.Form):
    rut = forms.CharField(
        label='Rut',
        max_length=12,
        widget=forms.TextInput(attrs={
            'placeholder': '12.345.678-9'
        })
    )

    nombre = forms.CharField(
        label='Nombre',
        max_length=100
    )

    apellido = forms.CharField(
        label='Apellido',
        max_length=100
    )

    fecha_nacimiento = forms.DateField(
        label='Fecha Nacimiento',
        input_formats=['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y'],  # Acepta DD-MM-AAAA, YYYY-MM-DD y DD/MM/AAAA
        widget=forms.TextInput(attrs={
            'class': 'datepicker',
            'placeholder': 'DD-MM-AAAA',
            'autocomplete': 'off'
        })
    )

    profesion = forms.CharField(
        label='Profesion',
        max_length=100
    )

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha:
            # Validar que la fecha no sea futura
            if fecha > date.today():
                raise forms.ValidationError('La fecha de nacimiento no puede ser futura.')

            # Validar edad mínima (por ejemplo, 18 años)
            edad = (date.today() - fecha).days // 365
            if edad < 18:
                raise forms.ValidationError('El profesor debe tener al menos 18 años.')

        return fecha

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        # Aquí podrías agregar validación de RUT chileno si lo necesitas
        return rut