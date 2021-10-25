from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainmenu),
    #cadastrar nova pessoa
    path('novapessoa/', views.novaPessoa, name='nova-pessoa'),
    #açoes com clientes
    path('clientes/', views.clientesList, name='cliente-list'),
    path('clientes/<int:id>', views.clienteView, name="cliente-view"),
    path('clientes/edit/<int:id>', views.editarCliente, name="editar-cliente"),
    path('clientes/delete/<int:id>', views.deletarCliente, name="deletar-cliente"),
    path('clientes/novocliente/', views.novoCliente, name="novo-cliente"),
    #açoes com reservas
    path('reservas/', views.reservaList, name='reserva-list'),
    path('reservas/novareserva/', views.novaReserva, name="nova-reserva"),
    path('reservas/edit/<int:id>', views.editarReserva, name="editar-reserva"),
    path('reservas/delete/<int:id>', views.deletarReserva, name="deletar-reserva"),
    path('reservas/<int:id>', views.reservaView, name="reserva-view"),
    #açoes com colaboradores
    path('colaboradores/', views.colaboradoresList, name='colaboradores-list'),
    path('colaboradores/<int:id>', views.colaboradorView, name="colaborador-view"),
    path('colaboradores/novocolaborador/', views.novoColaborador, name="novo-colaborador"),
    path('colaboradores/edit/<int:id>', views.editarColaborador, name="editar-colaborador"),
    path('colaboradores/delete/<int:id>', views.deletarColaborador, name="deletar-colaborador"),
]
