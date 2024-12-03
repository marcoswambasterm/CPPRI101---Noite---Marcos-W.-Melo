from django.db import models
from vitimas.models import Pessoa, PET
from voluntarios.models import Medico, Psicologo, Veterinario

class Atendimento(models.Model):
    TIPO_ATENDIMENTO_CHOICES = [
        ('Médico', 'Médico'),
        ('Psicológico', 'Psicológico'),
        ('Veterinário', 'Veterinário'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_ATENDIMENTO_CHOICES, default='Médico')
    descricao = models.TextField()
    data = models.DateField()
    medico = models.ForeignKey(
        Medico,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="atendimentos_medico"
    )
    psicologo = models.ForeignKey(
        Psicologo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="atendimentos_psicologo"
    )
    veterinario = models.ForeignKey(
        Veterinario,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="atendimentos_veterinario"
    )
    vitima_pessoa = models.ForeignKey(
        Pessoa,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="atendimentos_pessoa"
    )
    vitima_pet = models.ForeignKey(
        PET,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="atendimentos_pet"
    )

    def __str__(self):
        return f"Atendimento {self.tipo} em {self.data}"
