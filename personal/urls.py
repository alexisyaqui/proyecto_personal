
from django.urls import path
from .views import PersonaCreateView, PersonaUpateView, PersonaListView

urlpatterns = [
    path('crearpersona', PersonaCreateView.as_view(), name="crearpersona"),
    path('actualizarpersona', PersonaUpateView.as_view(), name="actualizarpersona"),
    path('listapersona', PersonaListView.as_view(), name="listapersona")
]
