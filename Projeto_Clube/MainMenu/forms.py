from django import forms

from .models import Cliente, Pessoa, Reserva, Colaborador, Dependente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('idPessoa', 'categoria', 'plano', 'status')

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'rg',
            'cpf',
            'rg',
            'telefone',
            'telefonecelular', 'datanascimento',
            'email',
            'foto',
        ]

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = [
            'idCliente',
            'local',
            'datareserva',
            'horareserva',
            'horareserva_fim',
        ]

class ColaboradorForm(forms.ModelForm):

    class Meta:
        model = Colaborador
        fields = ('idPessoa', 'permissao')
        
class DependenteForm(forms.ModelForm):
    
    class Meta:
        model = Dependente
        fields = [
            'idCliente',
            'nome',
            'rg',
            'parentesco',
            'datanascimento',
            'foto',
        ]