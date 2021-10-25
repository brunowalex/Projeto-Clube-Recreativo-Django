# Generated by Django 3.1.1 on 2021-10-25 13:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainMenu', '0005_auto_20211025_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='datareserva',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='horareserva',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainMenu.cliente', verbose_name='Nome'),
        ),
    ]