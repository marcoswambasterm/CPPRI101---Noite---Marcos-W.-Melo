from django import forms
from .models import Medico, Psicologo, Veterinario, Atendente

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'endereco', 'telefone', 'email', 'crm', 'especialidade']

class PsicologoForm(forms.ModelForm):
    class Meta:
        model = Psicologo
        fields = ['nome', 'endereco', 'telefone', 'email', 'crp']

class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nome', 'endereco', 'telefone', 'email', 'crmv']

class AtendenteForm(forms.ModelForm):
    class Meta:
        model = Atendente
        fields = ['nome', 'endereco', 'telefone', 'email', 'cpf']

