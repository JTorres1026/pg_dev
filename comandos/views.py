from django.shortcuts import render



def login_view(request):
    return render(request, 'login.html')



#Pantalla de inicio despues de logearse
def inicio_view(request):
    return render(request, 'inicio.html')


def crear_contenedor_view(request):
    return render(request, 'contenedor/crear_contenedor.html')