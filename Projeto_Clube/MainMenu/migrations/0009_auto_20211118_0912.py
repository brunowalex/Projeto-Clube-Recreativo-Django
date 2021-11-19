# Generated by Django 3.1.1 on 2021-11-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainMenu', '0008_auto_20211106_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCliente', models.CharField(help_text='max. 200 caracteres', max_length=200, verbose_name='Cliente')),
                ('nome', models.CharField(help_text='max. 200 caracteres', max_length=200, verbose_name='Nome')),
                ('rg', models.IntegerField(verbose_name='RG')),
                ('parentesco', models.CharField(help_text='max. 100 caracteres', max_length=100, verbose_name='Nome')),
                ('datanascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('foto', models.FileField(upload_to='', verbose_name='Foto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.IntegerField(verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='datanascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.FileField(upload_to='', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='rg',
            field=models.IntegerField(verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.BigIntegerField(verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefonecelular',
            field=models.BigIntegerField(verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='datareserva',
            field=models.DateField(verbose_name='Data da reserva'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horareserva',
            field=models.TimeField(verbose_name='Hora da reserva (Inicio)'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horareserva_fim',
            field=models.TimeField(verbose_name='Hora da reserva (Fim)'),
        ),
    ]