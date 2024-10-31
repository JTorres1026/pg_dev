from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views  # Importar las vistas que hemos creado

urlpatterns = [
    path('', views.login_view, name='vacia'), 
    path('login/', views.login_view, name='login'), #Iniciar sesión
    path('logout/', LogoutView.as_view(), name='logout'), #Cerrar sesión
    path('inicio/', views.inicio_view, name='inicio'),  # Ruta para la página principal
    path('crear-contenedor/', views.crear_contenedor_view, name='crear_contenedor'),
  
]