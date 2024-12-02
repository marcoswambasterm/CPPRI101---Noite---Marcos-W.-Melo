from django import forms
from .models import Atendimento
from vitimas.models import Pessoa, PET
from voluntarios.models import Medico, Psicologo, Veterinario


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['tipo', 'descricao', 'data', 'voluntario', 'psicologo', 'veterinario', 'vitima_pessoa', 'vitima_pet']

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')
        vitima_pessoa = cleaned_data.get('vitima_pessoa')
        vitima_pet = cleaned_data.get('vitima_pet')

        # Validação para garantir que atendimentos veterinários envolvem um pet
        if tipo == 'Veterinário' and not vitima_pet:
            raise forms.ValidationError("Atendimentos veterinários exigem um pet.")

        # Caso o tipo não seja veterinário, o pet não deve ser selecionado
        if tipo != 'Veterinário' and vitima_pet:
            raise forms.ValidationError("Este tipo de atendimento não podem envolver um pet.")

        return cleaned_data
