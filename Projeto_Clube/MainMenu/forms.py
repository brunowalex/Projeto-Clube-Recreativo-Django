from django import forms

from .models import Cliente, Pessoa, Reserva, Colaborador

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('idPessoa', 'categoria', 'plano', 'status')

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome', 'rg', 'cpf', 'telefone', 'telefonecelular', 'datanascimento', 'email', 'foto')

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('idCliente', 'local', 'datareserva', 'horareserva')

class ColaboradorForm(forms.ModelForm):

    class Meta:
        model = Colaborador
        fields = ('idPessoa', 'permissao')