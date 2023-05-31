from django import forms
from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            'nome_completo',
            'cpf',
            'data_nascimento',
            'numero_casa',
            'placa_veiculo',
        ]
        error_messages = {
            'nome_completo': {
                'required': 'O nome completo do visitante é obrigatório.'
            },
            'cpf': {
                'required': 'O CPF do visitante é obrigatório.'
            },
            'data_nascimento': {
                'required': 'A data de nascimento do visitante é obrigatória.',
                'invalid': 'Por favor, informe a data com um formato válido: (DD/MM/AAAA)'  # noqa E501
            },
            'numero_casa': {
                'required': 'O número da casa a ser visitada é obrigatório.',
            },
        }


class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model = Visitante
        fields = [
            'morador_responsavel'
        ]
        error_messages = {
            'morador_responsavel': {
                'required': 'Por favor, informe o nome do morador responsável.'
            }
        }
