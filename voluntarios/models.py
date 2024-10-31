from django.db import models

class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class Medico(Voluntario):
    crm = models.CharField(max_length=20)


    ESPECIALIDADES = [
        ('Cardiologia', 'Cardiologia'),
        ('Dermatologia', 'Dermatologia'),
        ('Ginecologia', 'Ginecologia'),
        ('Neurologia', 'Neurologia'),
        ('Ortopedia', 'Ortopedia'),
        ('Pediatria', 'Pediatria'),
        ('Psiquiatria', 'Psiquiatria'),
        ('Urologia', 'Urologia'),
    ]

    especialidade = models.CharField(
        max_length=50,
        choices=ESPECIALIDADES,
    )

class Psicologo(Voluntario):
    crp = models.CharField(max_length=20)

class Veterinario(Voluntario):
    crmv = models.CharField(max_length=20)

class Atendente(Voluntario):
    cpf = models.CharField(max_length=11)
