from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Titulo = models.CharField(max_length=200)
    Contenido = models.TextField()
    Fecha_de_Publicacion = models.DateTimeField(auto_now_add=True)
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)
    

