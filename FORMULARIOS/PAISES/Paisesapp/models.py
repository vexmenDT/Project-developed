from django.db import models

class Paises (models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Estados (models.Model):
    nombre= models.CharField(max_length=50)
    pais= models.ForeignKey(Paises,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Alumnos(models.Model):
    nombre= models.CharField(max_length=50)
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE)



# Create your models here.
