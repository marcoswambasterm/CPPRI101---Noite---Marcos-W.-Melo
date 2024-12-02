from django import forms
from abrigos.models import Abrigo


class AbrigoForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = ['nome', 'endereco', 'capacidade', 'telefone', 'email']

        error_messages = {
            'capacidade': {'min_value': 'Capacidade minínima do abrigo não pode ser menor que 01',
                           'max_value': 'Capacidade máxima do abrigo não pode ser maior que 100',}

        }