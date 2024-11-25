from django.urls import path
from materia_app import views
urlpatterns = [
    path("",views.inicio_vista,name="inicio_vista"),
    path("registrarComic/",views.registrarMateria,name="registrarMateria"),
    path("borrarComic/<codigo>",views.borrarMateria,name="borrarMateria"),
    path("seleccionarcomic/<codigo>",views.seleccionarmateria,name="seleccionarmateria"),
    path("editarComic/", views.editarMateria, name='editarMateria'),
]
