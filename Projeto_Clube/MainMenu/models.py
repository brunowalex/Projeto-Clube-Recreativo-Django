from django.db import models

#Pessoa

class Pessoa(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=200, help_text='max. 200 caracteres')
    rg = models.IntegerField()
    cpf = models.IntegerField()
    telefone = models.BigIntegerField()
    telefonecelular = models.BigIntegerField()
    datanascimento = models.DateField()
    foto = models.FileField()
    email = models.EmailField()  
    
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
        return self.idPessoa

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
    datareserva = models.DateField(blank=True, null=True)
    horareserva = models.TimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.local

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
        return self.idPessoa

