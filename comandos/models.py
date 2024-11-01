from django.db import models
from django.contrib.auth.models import User  # Importa el modelo User de Django

class Categoria(models.Model):
  # Campo de categoría, con un máximo de 30 caracteres
    categoria = models.CharField(max_length=30)
    
    def __str__(self):
        return self.categoria  # Para que en el panel de administración se muestre el nombre de la categoría




class Comando(models.Model):

    # Campo de comando con un límite de 20 caracteres
    comando = models.CharField(max_length=20)
    
    # Campo de descripción con un límite de 20 caracteres
    descripcion = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.comando} - {self.descripcion}"  # Para mostrar el comando y su descripción en el admin




class Subcomando(models.Model):
    
    # Campo de subcomando con un límite de 30 caracteres
    subcomando = models.CharField(max_length=30)
    
    # Clave foránea que se relaciona con la tabla Categoria
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.subcomando} (Categoría: {self.categoria})"


class Opcion(models.Model):
    
    # Campo de opcion con un límite de 30 caracteres
    opcion = models.CharField(max_length=30)
    
    # Campo de descripción con un límite de 100 caracteres
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.opcion} - {self.descripcion[:50]}..."  # Muestra el nombre de la opción y parte de la descripción en el admin






class Historial(models.Model):
    
    # Campo de comando con un límite de 200 caracteres
    comando = models.CharField(max_length=300, null=False)
    
    # Campo de fecha, configurado para almacenar la fecha actual por defecto
    fecha = models.DateField(auto_now_add=True, null=False)
    
    # Relación con el usuario que realizó el comando
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return f"Comando: {self.comando} - Usuario: {self.usuario.username} - Fecha: {self.fecha}"





