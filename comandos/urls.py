from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views  # Importar las vistas que hemos creado

urlpatterns = [
    path('', views.login_view, name='vacia'), 
    path('login/', views.login_view, name='login'), #Iniciar sesión
    path('logout/', LogoutView.as_view(), name='logout'), #Cerrar sesión
    path('inicio/', views.inicio_view, name='inicio'),  # Ruta para la página principal
    path('registro/', views.registro_view, name='registro'),
    path('actualizar-usuario/', views.editar_perfil_view, name='actualizar'),

    #Operaciones con contenedores
    path('crear-contenedor/', views.crear_contenedor_view, name='crear_contenedor'),
    path('acciones-contenedor/', views.acciones_contenedor_view, name='acciones_contenedor'),

    #Operaciones con imágenes
    path('crear-imagen/', views.crear_imagen_view, name='crear_imagen'),
    path('acciones-imagen/', views.acciones_imagen_view, name='acciones_imagen'),

    #historial de comandos
    path('historial/', views.historial_view, name='historial'),

    #comandos rapidos
    path('comandos-rapidos/', views.comandos_rapidos_view, name='comandos_rapidos'),

  
]