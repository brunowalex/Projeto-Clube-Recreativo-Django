# Generated by Django 3.1.1 on 2021-10-25 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainMenu', '0004_colaborador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainMenu.cliente'),
        ),
    ]
