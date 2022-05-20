from pyexpat import model
from django.db import models

# Create your models here.

class persona(models.Model):
    prim_nombre = models.CharField(max_length=50)
    seg_nombre = models.CharField(max_length=50)
    prim_apellido = models.CharField(max_length=50)
    seg_apellido = models.CharField(max_length=50)
    dpi = models.IntegerField()
    nit = models.IntegerField()
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=450)
    aldea = models.CharField(max_length=250)
    municipio = models.CharField(max_length=250)
    departamento = models.CharField(max_length=250)
    genero = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='images/', verbose_name='')
 
    def __str__(self):
        return self.prim_nombre
