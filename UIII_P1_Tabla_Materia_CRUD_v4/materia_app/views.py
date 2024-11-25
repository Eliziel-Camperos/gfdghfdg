from django.shortcuts import render,redirect
from .models import Materia

# Create your views here.

def inicio_vista(request):
    lasmateria=Materia.objects.all()
    return render(request, "gestionarmateria.html",{"mismaterias":lasmateria})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    guardarmateria=Materia.objects.create(
        codigo=codigo,nombre=nombre,creditos=creditos
    )

    return redirect("/")

def seleccionarmateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"mismaterias":materia})

def editarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    Materia.nombre=nombre
    Materia.creditos=creditos
    Materia.save()
    return redirect("/")

def borrarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete()
    return redirect("/")
