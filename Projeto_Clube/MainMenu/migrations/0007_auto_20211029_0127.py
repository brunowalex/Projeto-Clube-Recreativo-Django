# Generated by Django 3.1.1 on 2021-10-29 04:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainMenu', '0006_auto_20211025_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
