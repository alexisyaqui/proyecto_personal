
from cProfile import label
from attr import attr, attrs
from django import forms
from matplotlib import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = persona
        fields = ('prim_nombre', 'seg_nombre', 'prim_apellido', 'seg_apellido', 'dpi', 'nit', 'fecha_nac', 'telefono', 'email', 
                    'direccion', 'aldea', 'municipio', 'departamento', 'genero', 'foto')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('Submit', 'GUARDAR PERSONA'))


"""""
        labels= {
            'prim_nombre': 'Primer Nombre',
            'seg_nombre': 'Segundo Nombre',
            'prim_apellido': 'Primer Apellido',
            'seg_apellido': 'Segundo Apellido',
            'dpi': 'Documento Personal de Identificacion (DPI)',
            'nit': 'Numero de Identificación Tributario (NIT)',
            'fecha_nac': 'Fecha de Nacimiento',
            'telefono': 'Numero de Telefono',
            'email': 'Correo Electronico',
            'direccion': 'Direccion Domiciliar',
            'aldea': 'Aldea',
            'municipio': 'Municipio',
            'departamento': 'Departamento',
            'genero': 'Genero',
            'foto': 'Fotografia personal',

        }

        widgets= {
            'prim_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'seg_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'prim_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'seg_apellido':  forms.TextInput(attrs={'class': 'form-control'}),
            'dpi':  forms.TextInput(attrs={'class': 'form-control'}),
            'nit': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nac': forms.DateField(attrs={'class': 'form-control'}),
            'telefono': 'Numero de Telefono',
            'email': 'Correo Electronico',
            'direccion': 'Direccion Domiciliar',
            'aldea': 'Aldea',
            'municipio': 'Municipio',
            'departamento': 'Departamento',
            'genero': 'Genero',
            'foto': 'Fotografia personal',

        }
"""
