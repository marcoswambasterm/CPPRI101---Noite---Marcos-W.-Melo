from django.db import models

# Create your models here.

# Classe base Vítima
class Vitima(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    idade = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

# Subclasse Pessoa
class Pessoa(Vitima):
    sexo = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

# Subclasse PET
class PET(Vitima):
    raca = models.CharField(max_length=50)
