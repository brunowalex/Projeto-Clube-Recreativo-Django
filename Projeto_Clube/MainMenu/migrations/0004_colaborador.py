# Generated by Django 3.1.1 on 2021-10-25 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainMenu', '0003_auto_20211025_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissao', models.CharField(choices=[('usuario', 'Usuario'), ('administrador', 'Administrador')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('idPessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainMenu.pessoa', verbose_name='Nome')),
            ],
        ),
    ]
