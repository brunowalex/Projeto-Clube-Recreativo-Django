from django.contrib import admin

from .models import Cliente, Pessoa, Reserva, Colaborador

admin.site.register(Cliente)
admin.site.register(Pessoa)
admin.site.register(Reserva)
admin.site.register(Colaborador)