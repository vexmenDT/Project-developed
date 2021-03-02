from django.shortcuts import render, redirect
from .models import Estados, Paises, Alumnos
from .forms import PaisF, EstadosF , AlumnosF

def CrearA(request):
    template = 'Paisesapp/Formulario.html'
    informacion = Alumnos.objects.all()
    data ={
        'data': AlumnosF(),
        'info':informacion
    }

    if request.method == 'POST':
        formulario = AlumnosF(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='Alumno')

    return render(request,template, data)

def CrearPA(request):
    template = 'Paisesapp/Formulario2.html'
    informacion = Paises.objects.all()
    data ={
        'data': PaisF(),
        'info':informacion
    }

    if request.method == 'POST':
        formulario = PaisF(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='Pais')

    return render(request,template, data)



def CrearE(request):
    template = 'Paisesapp/Formulario3.html'
    informacion = Estados.objects.all()
    data ={
        'data': EstadosF(),
        'info':informacion
    }

    if request.method == 'POST':
        formulario = EstadosF(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='Estado')

    return render(request,template, data)







#Metodo para generar ajax y ingresar los estados dependientes del pais


def load_cities(request):
    pais_id = request.GET.get('pais_id')
    estado = Estados.objects.filter(pais_id=pais_id).all()
    return render(request, 'Paisesapp/city_dropdown_list_options.html', {'estado': estado})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
