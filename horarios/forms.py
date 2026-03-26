from django import forms
from .models import Asignatura, BloqueHorario


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'codigo', 'color']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
                'placeholder': 'Ej: Matemáticas'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
                'placeholder': 'Ej: MAT'
            }),
            'color': forms.Select(
                choices=[
                    ('blue', 'Azul'),
                    ('indigo', 'Índigo'),
                    ('purple', 'Púrpura'),
                    ('rose', 'Rosa'),
                    ('red', 'Rojo'),
                    ('amber', 'Ámbar'),
                    ('green', 'Verde'),
                    ('emerald', 'Esmeralda'),
                    ('teal', 'Teal'),
                    ('cyan', 'Cyan'),
                    ('slate', 'Gris'),
                ],
                attrs={
                    'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
                }
            ),
        }


class BloqueHorarioForm(forms.ModelForm):
    class Meta:
        model = BloqueHorario
        fields = ['curso', 'asignatura', 'profesor', 'dia_semana', 'hora_inicio', 'hora_fin', 'sala']
        widgets = {
            'curso': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
            }),
            'asignatura': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
            }),
            'profesor': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
            }),
            'dia_semana': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
            }),
            'hora_inicio': forms.TimeInput(format='%H:%M', attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
                'type': 'time',
            }),
            'hora_fin': forms.TimeInput(format='%H:%M', attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
                'type': 'time',
            }),
            'sala': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#002147] focus:border-transparent text-slate-800',
                'placeholder': 'Ej: Sala 12 (opcional)'
            }),
        }