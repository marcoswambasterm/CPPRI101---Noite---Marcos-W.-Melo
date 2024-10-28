from django import forms
from .models import Pessoa, PET

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'endereco', 'idade', 'sexo', 'telefone', 'email']

class PetForm(forms.ModelForm):
    class Meta:
        model = PET
        fields = ['nome', 'endereco', 'idade', 'raca', 'especie', 'dono']
