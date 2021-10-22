from django.db import models
from apps import mantenimiento
from apps.equipo.models  import Equipo
from apps.mantenimiento.models import Mantenimiento

# Create your models here.

class Mantenimiento_equipo(models.Model):

    mantenimiento    = models.ForeignKey(Mantenimiento, on_delete= models.CASCADE)
    equipo           =models.ForeignKey(Equipo, on_delete= models.CASCADE)
    Descripcion      =models.CharField(max_length= 50)
    Resultado        =models.BooleanField()



    def __str__(self):
        return self.Descripcion
