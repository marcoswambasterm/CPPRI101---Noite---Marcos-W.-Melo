from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Abrigo(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    capacidade = models.PositiveIntegerField(
        verbose_name="Capacidade Máxima",
        validators=[
            MinValueValidator(1),  # Valor mínimo: 1
            MaxValueValidator(100)  # Valor máximo: 100
        ]
    )
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome
