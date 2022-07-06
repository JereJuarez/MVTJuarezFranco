from django.db import models

# Create your models here.
class familiares(models.Model):

    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=40)
    cuadro=models.CharField(max_length=35)
    fecha_nacimiento=models.DateField()
