from django import forms
from .models import Apoderado

TAILWIND_INPUT = 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white text-slate-900 focus:ring-2 focus:ring-[#002147] focus:border-[#002147] outline-none transition-all'


class ApoderadoForm(forms.ModelForm):

    class Meta:
        model = Apoderado
        fields = ['rut', 'nombre', 'apellido', 'telefono', 'email', 'direccion', 'alumnos']
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': '12.345.678-9',
            }),
            'nombre': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Ingrese el nombre',
            }),
            'apellido': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Ingrese el apellido',
            }),
            'telefono': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': '+56 9 1234 5678',
            }),
            'email': forms.EmailInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'correo@ejemplo.com',
            }),
            'direccion': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Dirección opcional',
            }),
            'alumnos': forms.SelectMultiple(attrs={
                'class': TAILWIND_INPUT,
                'size': '5',
            }),
        }

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if rut:
            rut = rut.strip()
            if len(rut) < 9:
                raise forms.ValidationError('Ingrese un RUT válido.')
        return rut
