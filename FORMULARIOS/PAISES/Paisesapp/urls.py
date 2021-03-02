from django.urls import path
from .views import CrearA , load_cities , CrearPA, CrearE
urlpatterns = [
path ('Pais/', CrearPA , name='Pais'),
path ('Estado/', CrearE , name='Estado'),
path ('Alumno/', CrearA , name='Alumno'),




path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]