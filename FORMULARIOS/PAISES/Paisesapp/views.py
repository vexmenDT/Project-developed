from django.shortcuts import render

def primera(request): #El request es la petición, render pinta mi templates

    templates = 'Paisesapp/Formulario.html'

    return render(request,templates)

# Create your views here.
