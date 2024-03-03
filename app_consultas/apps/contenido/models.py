from django.db import models

class Media(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='media/')  # Ruta donde se guardarán los archivos
    comentario = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
