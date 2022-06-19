from django.urls import path
from .views import home, acerca, subida, mortalidad, media_desvistd, mayorescasos, menorescasos, prommuerte, promrecuperacion, diagramapastel


urlpatterns = [
    path('', home, name='index'),
    path('AcercaDe/', acerca, name='acerca'),
    path('Subida/', subida, name='subida'),
    path('Mortalidad/', mortalidad, name='mortalidad'),
    path('DiagPastel/', diagramapastel, name='diagramapastel'),
    path('MediDesvSTD/', media_desvistd, name='media_desvistd'),
    path('MayoresCasos/', mayorescasos, name='mayorescasos'),
    path('MenoresCasos/', menorescasos, name='menorescasos'),
    path('PromRecuper/', promrecuperacion, name='promrecuperacion'),
    path('PromMuerte/', prommuerte, name='prommuerte'),
]