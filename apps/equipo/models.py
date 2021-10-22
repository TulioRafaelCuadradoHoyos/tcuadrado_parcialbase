from django.db import models

# Create your models here.

class Equipo(models.Model):

    Fecha           =models.DateField()
    Solicitud       =models.IntegerField()
    Tiempo_atencion =models.IntegerField()



    def __str__(self):
        return self.Solicitud