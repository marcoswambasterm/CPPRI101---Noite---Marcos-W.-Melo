from django.db import models

# Create your models here.

class Abrigo(models.Model):
    endereco = models.CharField(max_length=255)
    capacidade_maxima = models.IntegerField()
    capacidade_maxima_voluntarios = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Abrigo em {self.endereco}"

class AbrigoComAnimais(Abrigo):
    capacidade_maxima_animais = models.IntegerField()
