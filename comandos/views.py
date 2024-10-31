from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    return render(request, 'contenedor/crear_contenedor.html')