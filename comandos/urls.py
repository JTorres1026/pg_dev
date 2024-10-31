from django.urls import path
from . import views  # Importar las vistas que hemos creado

urlpatterns = [
    path('', views.login_view, name='vacia'), 
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio_view, name='inicio'),  # Ruta para la página principal
    path('crear-contenedor/', views.crear_contenedor_view, name='crear_contenedor'),
  
]