from django import forms
from abrigos.models import Abrigo


class AbrigoForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = ['nome', 'endereco', 'capacidade', 'telefone', 'email']

        error_messages = {
            'capacidade': {'min_value': 'Valor minimo',
                           'max_value': 'Valor Maximo',}

        }