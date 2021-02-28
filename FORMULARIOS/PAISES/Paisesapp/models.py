from django.db import models

class Paises (models.Model):
    NombreP = models.CharField(max_length=50)

class Estados (models.Model):
    NombreE= models.CharField(max_length=50)
    Pais= models.ForeignKey(Paises,on_delete=models.CASCADE)

    def __init__(self):

        return self
# Create your models here.
