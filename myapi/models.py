from django.db import models

# Create your models here.

class Gestante(models.Model):
    name = models.CharField(max_length=60)
    mae = models.CharField(max_length=60)
    dn = models.DateField
    cpf = models.IntegerField
    cns = models.IntegerField
    endereco = models.CharField(max_length=150)
    unidade = models.CharField(max_length=60)
    empresa = models.CharField(max_length=60)
    def __str__(self):
        return self.name
        

