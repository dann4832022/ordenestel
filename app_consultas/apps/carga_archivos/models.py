from django.db import models

class ArchivoExcel(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(null=True)
    linea = models.IntegerField(null=True)
    orden = models.CharField(max_length=50)
    fecha_de_cita = models.DateField(null=True)
    motivo_t3 = models.CharField(max_length=100)
    representante = models.CharField(max_length=100)
    lider = models.CharField(max_length=100)
    devolucion = models.BooleanField(default=False)
    archivo = models.FileField(upload_to='archivos_excel/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Archivo Excel: {self.fecha} - {self.linea} - {self.orden}'
