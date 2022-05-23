
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import persona


class PersonaForm(forms.ModelForm):

    prim_nombre = forms.CharField(label='PRIMER NOMBRE', max_length=50)
    seg_nombre = forms.CharField(max_length=50)
    prim_apellido = forms.CharField(max_length=50)
    seg_apellido = forms.CharField(max_length=50)
    dpi = forms.IntegerField()
    nit = forms.IntegerField()
    fecha_nac = forms.DateField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    direccion = forms.CharField(max_length=450)
    aldea = forms.CharField(max_length=250)
    municipio = forms.CharField(max_length=250)
    departamento = forms.CharField(max_length=250)
    genero = forms.CharField(max_length=12)
    foto = forms.ImageField()
 


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('Submit', 'GUARDAR PERSONA'))


