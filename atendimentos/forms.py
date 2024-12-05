from django import forms
from .models import Atendimento
from vitimas.models import Pessoa, PET
from voluntarios.models import Medico, Psicologo, Veterinario, Atendente
from abrigos.models import Abrigo


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['tipo', 'descricao', 'data', 'medico', 'psicologo', 'veterinario', 'atendente', 'vitima_pessoa', 'vitima_pet', 'abrigo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['atendente'].queryset = Atendente.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')
        medico = cleaned_data.get('medico')
        psicologo = cleaned_data.get('psicologo')
        veterinario = cleaned_data.get('veterinario')
        atendente = cleaned_data.get('atendente')
        vitima_pessoa = cleaned_data.get('vitima_pessoa')
        vitima_pet = cleaned_data.get('vitima_pet')
        abrigo = cleaned_data.get('abrigo')

        # Validação para garantir que o voluntário corresponde ao tipo de atendimento
        if tipo == 'Médico' and not medico:
            raise forms.ValidationError("Atendimentos médicos exigem a seleção de um médico.")
        if tipo == 'Psicológico' and not psicologo:
            raise forms.ValidationError("Atendimentos psicológicos exigem a seleção de um psicólogo.")
        if tipo == 'Veterinário' and not veterinario:
            raise forms.ValidationError("Atendimentos veterinários exigem a seleção de um veterinário.")

        # Validação para garantir que atendimentos veterinários envolvem um pet
        if tipo == 'Veterinário' and not vitima_pet:
            raise forms.ValidationError("Atendimentos veterinários exigem a seleção de um pet.")

        # Validação para evitar a seleção de uma vítima pessoa junto com um atendimento veterinário
        if tipo == 'Veterinário' and veterinario and vitima_pessoa:
            raise forms.ValidationError("Atendimentos veterinários não podem envolver uma vítima do tipo pessoa.")

        # Validações de alocação
        if tipo == 'Alocação':
            if not atendente:
                raise forms.ValidationError("Atendimentos de alocação exigem a seleção de um atendente.")
            if not abrigo:
                raise forms.ValidationError("Selecione um abrigo para alocar a vítima.")
            if vitima_pessoa is None and vitima_pet is None:
                raise forms.ValidationError("Selecione uma vítima (pessoa ou pet) para alocação.")
            if abrigo and abrigo.capacidade <= 0:
                raise forms.ValidationError("O abrigo selecionado está lotado.")

        # Remover seleções inválidas de voluntários
        if tipo != 'Médico':
            cleaned_data['medico'] = None
        if tipo != 'Psicológico':
            cleaned_data['psicologo'] = None
        if tipo != 'Veterinário':
            cleaned_data['veterinario'] = None
        if tipo != 'Alocação':
            cleaned_data['abrigo'] = None
            cleaned_data['atendente'] = None

        return cleaned_data