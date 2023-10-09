from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    imagen = models.ImageField(upload_to='profiles')
    
    def __str__(self):
        return f'{self.id} - {self.user}' 
    
class Celular(models.Model):
    #series = [('serie A', 'Serie A')
              #('serie S', 'Serie S')
              #('serie Z', 'Serie Z')
              #('serie M', 'Serie M')
              #]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=40)
    serie = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits= 8, decimal_places=2)
    memoria = models.CharField(max_length=20)
    pantalla = models.DecimalField(max_digits=2, decimal_places=1)
    camara = models.DecimalField(max_digits=3, decimal_places=1)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagenCelular = models.ImageField(null=True, blank=True, upload_to="media")
    
    def str(self):
        return f'{self.id} {self.nombre} {self.serie} {self.precio} {self.memoria}'

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']
    
    
class Post(models.Model):
    
    post =models.ForeignKey(User, on_delete=models.CASCADE, related_name='Post', null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.post)
    