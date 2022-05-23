
from django.urls import path
from .views import InicioListview, PersonaCreateView, PersonaUpateView, PersonaListView

urlpatterns = [
    path('', InicioListview.as_view(), name="inicio"),
    path('crearpersona', PersonaCreateView.as_view(), name="crearpersona"),
    path('listapersona', PersonaListView.as_view(), name="listapersona")
]
