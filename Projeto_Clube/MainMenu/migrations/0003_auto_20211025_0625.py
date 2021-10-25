# Generated by Django 3.1.1 on 2021-10-25 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainMenu', '0002_auto_20211024_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainMenu.pessoa'),
        ),
    ]