from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Opcion, Comando, Historial,Subcomando


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

        #Creación del comando

        #obtener comando
        icomando = Comando.objects.get(descripcion='basico')
        nombrec = icomando.comando

        #obtener subcomando
        subcomando = Subcomando.objects.get(subcomando='run')
        sub= subcomando.subcomando

        #obtener la opcion de nombre 
        fnombre= Opcion.objects.get(descripcion='nombre')
        opcion_nombre= fnombre.opcion
        

        if modo_ejecucion=='si':
            #obtener la opción de segundo plano
            segundo_plano = Opcion.objects.get(descripcion='segundoplano')
            opcion_segundo_plano= segundo_plano.opcion

            comando= f"{nombrec} {sub} {opcion_nombre} {nombre_contenedor} {opcion_segundo_plano} {nombre_imagen}"

            if tiene_puerto=='si':
                
                opcion_puerto= Opcion.objects.get(descripcion='puerto')

                comando= f"{nombrec} {sub} {opcion_nombre} {nombre_contenedor} {opcion_segundo_plano} {opcion_puerto.opcion} {puerto_host}:{puerto_contenedor} {nombre_imagen}"


        else:

            if tiene_puerto=='si':
                
                opcion_puerto= Opcion.objects.get(descripcion='puerto')

                comando= f"{nombrec} {sub} {opcion_nombre} {nombre_contenedor} {opcion_puerto.opcion} {puerto_host}:{puerto_contenedor} {nombre_imagen}"
            
            else:
                comando= f"{nombrec} {sub} {opcion_nombre} {nombre_contenedor} {nombre_imagen}"


        print(nombre_contenedor,nombre_imagen,modo_ejecucion, tiene_puerto,puerto_host,puerto_contenedor)        
   

        
        return render(request, 'contenedor/crear_contenedor.html', {'comando': comando })
    
    return render(request, 'contenedor/crear_contenedor.html')



@login_required
def acciones_contenedor_view(request):
    if request.method == 'POST':
        nombre_contenedor = request.POST.get('nombre_contenedor')
        accion = request.POST.get('accion')
        

        #Creación del comando

        

        #obtener comando
        icomando = Comando.objects.get(descripcion='basico')
        nombrec = icomando.comando

        if accion=='iniciar':
            #obtener subcomando
            subcomando = Subcomando.objects.get(subcomando='start')
            sub= subcomando.subcomando

            comando= f"{nombrec} {sub} {nombre_contenedor}"

        if accion=='detener':
            #obtener subcomando
            subcomando = Subcomando.objects.get(subcomando='stop')
            sub= subcomando.subcomando

            comando= f"{nombrec} {sub} {nombre_contenedor}"    
        
        if accion=='reiniciar':
            #obtener subcomando
            subcomando = Subcomando.objects.get(subcomando='restart')
            sub= subcomando.subcomando

            comando= f"{nombrec} {sub} {nombre_contenedor}"


        if accion=='interactuar':
            #obtener subcomando
            subcomando = Subcomando.objects.get(subcomando='exec')
            sub= subcomando.subcomando

            opcion = Opcion.objects.get(descripcion='interactivo')

            comando= f"{nombrec} {sub} {opcion.opcion} {nombre_contenedor} bash"

        
        if accion=='eliminar':
            #obtener subcomando
            subcomando = Subcomando.objects.get(subcomando='rm')
            sub= subcomando.subcomando

            comando= f"{nombrec} {sub} {nombre_contenedor}"
        
        return render(request, 'contenedor/acciones_contenedor.html', {'comando': comando })
    
    return render(request, 'contenedor/acciones_contenedor.html')