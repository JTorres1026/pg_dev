from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


#Controlar el inicio de sesión

def login_view(request):

    if request.method == 'POST':
        username = request.POST['user_email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirige a la página de inicio o al dashboard
        else:
            messages.error(request, 'Credenciales incorrectas')


    return render(request, 'login.html')






#Pantalla de inicio despues de logearse
@login_required
def inicio_view(request):
    return render(request, 'inicio.html')




@login_required
def crear_contenedor_view(request):

    if request.method == 'POST':
        nombre_contenedor = request.POST.get('nombre_contenedor')
        nombre_imagen = request.POST.get('nombre_imagen')
        modo_ejecucion = request.POST.get('modo_ejecucion')
        tiene_puerto = request.POST.get('tiene_puerto')
        puerto_host = request.POST.get('puerto_host')
        puerto_contenedor = request.POST.get('puerto_contenedor')
                
        print(nombre_contenedor,nombre_imagen,modo_ejecucion, tiene_puerto,puerto_host,puerto_contenedor)        
        # procesar los datos o guardarlos en la base de datos
        comando = 'El nombre de tu contenedor sera '+nombre_contenedor

        
        return render(request, 'contenedor/crear_contenedor.html', {'comando': comando })
    
    return render(request, 'contenedor/crear_contenedor.html')