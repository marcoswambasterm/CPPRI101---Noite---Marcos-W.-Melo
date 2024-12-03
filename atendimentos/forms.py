from django import forms
from .models import Atendimento
from vitimas.models import Pessoa, PET
from voluntarios.models import Medico, Psicologo, Veterinario


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['tipo', 'descricao', 'data', 'medico', 'psicologo', 'veterinario', 'vitima_pessoa', 'vitima_pet']

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')
        medico = cleaned_data.get('medico')
        psicologo = cleaned_data.get('psicologo')
        veterinario = cleaned_data.get('veterinario')
        vitima_pessoa = cleaned_data.get('vitima_pessoa')
        vitima_pet = cleaned_data.get('vitima_pet')

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

        # Caso o tipo não seja veterinário, o pet não deve ser selecionado
        if tipo != 'Veterinário' and vitima_pet:
            raise forms.ValidationError("Atendimentos médicos ou psicológicos não podem envolver um pet.")

        # Remover seleções inválidas de voluntários
        if tipo != 'Médico':
            cleaned_data['medico'] = None
        if tipo != 'Psicológico':
            cleaned_data['psicologo'] = None
        if tipo != 'Veterinário':
            cleaned_data['veterinario'] = None

        return cleaned_data
