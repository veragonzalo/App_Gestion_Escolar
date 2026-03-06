from django.db import models

class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.codigo} {self.nombre}'





# Create your models here.
