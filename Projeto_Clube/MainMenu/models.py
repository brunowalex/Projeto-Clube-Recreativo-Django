from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.urls import reverse

#Pessoa

class Pessoa(models.Model):
    nome = models.CharField(blank=False, null=False, verbose_name='Nome', max_length=200, help_text='max. 200 caracteres')
    rg = models.IntegerField(blank=False, null=False, verbose_name='RG')
    cpf = models.IntegerField(blank=False, null=False, verbose_name="CPF")
    telefone = models.BigIntegerField(blank=False, null=False, verbose_name="Telefone")
    telefonecelular = models.BigIntegerField(blank=False, null=False, verbose_name="Celular")
    datanascimento = models.DateField(blank=False, null=False, verbose_name="Data de Nascimento")
    foto = models.FileField(blank=False, null=False, verbose_name="Foto")
    email = models.EmailField(blank=False, null=False, verbose_name="E-mail")  
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.nome     

#Clientes

class Cliente(models.Model):

    STATUSCATEGORIA = (
        ('socio', 'Socio'),
        ('aluno', 'Aluno'),
        ('socio e aluno', 'Socio e Aluno'),
    )

    STATUSSTATUS = (
        ('regular', 'Regular'),
        ('irregular', 'Irregular'),
    )

    STATUSPLANO = (
        ('individual', 'Individual'),
        ('familiar', 'Familiar'),
    )

    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Nome')
    categoria = models.CharField(
        max_length=255,
        choices=STATUSCATEGORIA,
    )
    plano = models.CharField(
        max_length=255,
        choices=STATUSPLANO,
    )
    status =  models.CharField(
        max_length=255,
        choices=STATUSSTATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
         
    def __str__ (self):
        return str(self.idPessoa)

#Reservas

class Reserva(models.Model):

    STATUSLOCAL = (
        ('quadra de tênis', 'Quadra de Tênis'),
        ('natação', 'Natação'),
        ('quadra de tênis (saibro)', 'Quadra de Tênis (Saibro)'),
        ('academia', 'Academia'),
    )

    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Nome') 
    
    local = models.CharField(
        max_length=255,
        choices=STATUSLOCAL,
    )
    datareserva = models.DateField(blank=False, null=False, verbose_name="Data da reserva")
    horareserva = models.TimeField(blank=False, null=False, verbose_name="Hora da reserva (Inicio)")
    horareserva_fim = models.TimeField(blank=False, null=False, verbose_name="Hora da reserva (Fim)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return str(self.idCliente)

#Colaboradores

class Colaborador(models.Model):

    TIPOPERMISSAO = (
        ('usuario', 'Usuario'),
        ('administrador', 'Administrador'),
    )

    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Nome')
    permissao = models.CharField(
        max_length=255,
        choices=TIPOPERMISSAO,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return str(self.idPessoa)