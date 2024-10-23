from django.shortcuts import render

def inicio_view(request):
    return render(request, 'inicio.html')


def crear_contenedor_view(request):
    return render(request, 'contenedor/crear_contenedor.html')