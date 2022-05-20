
from django.views.generic import CreateView, UpdateView, ListView
from .models import *
from .forms import PersonaForm



class PersonaCreateView(CreateView):
    model = persona
    fields = ('prim_nombre', 'seg_nombre', 'prim_apellido', 'seg_apellido', 'dpi', 'nit', 'fecha_nac', 'telefono', 'email', 'direccion', 'aldea', 'municipio', 'departamento', 'genero', 'foto')

    template_name = './persona_form.html'


class PersonaUpateView(UpdateView):
    model = persona
    form_class: PersonaForm

    template_name = './persona_update.html'

class PersonaListView(ListView):
    model = persona
    form_class: PersonaForm

    template_name = './persona_list.html'