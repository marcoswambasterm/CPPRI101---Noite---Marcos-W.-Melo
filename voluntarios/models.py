from django.db import models

# Create your models here.

class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        abstract = True

class Medico(Voluntario):
    crm = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=50)

class Psicologo(Voluntario):
    crp = models.CharField(max_length=20)

class Veterinario(Voluntario):
    crmv = models.CharField(max_length=20)

class Atendente(Voluntario):
    cpf = models.CharField(max_length=11)