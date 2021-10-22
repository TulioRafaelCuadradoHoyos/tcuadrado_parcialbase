from django.db import models

# Create your models here.

class Mantenimiento(models.Model):

    Nombre      =models.CharField(max_length=50)
    Marca       =models.CharField(max_length= 50)
    Modelo      =models.CharField(max_length= 50)



    def __str__(self):
        return self.Modelo
