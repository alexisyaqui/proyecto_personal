from django.views.generic import CreateView, UpdateView, ListView
from .models import *
from .forms import PersonaForm

class InicioListview(ListView):

    model = inicio
    fields = '__all__'

    template_name = './inicio/inicio_list.html'


class PersonaCreateView(CreateView):
    model = persona
    fields = '__all__'
    template_name = './persona_form.html'


class PersonaUpateView(UpdateView):
    model = persona
    form_class: PersonaForm

    template_name = './persona_update.html'

class PersonaListView(ListView):

    model = persona

    template_name = './persona_view.html'