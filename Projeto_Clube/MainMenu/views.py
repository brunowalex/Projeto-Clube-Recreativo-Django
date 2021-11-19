from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClienteForm, PessoaForm, ReservaForm, ColaboradorForm, DependenteForm
from django.contrib.auth.decorators import login_required

from .models import Cliente, Dependente, Pessoa, Reserva, Colaborador, Dependente
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone

@login_required
def mainmenu(request):
    search = request.GET.get('search')

    if search:

        reservas = Reserva.objects.filter(datareserva=search)

    else:
        
        now = timezone.now()   
        
        reserva_list = Reserva.objects.filter(datareserva__gte=now).order_by('datareserva')

        paginator = Paginator(reserva_list, 2)

        page = request.GET.get('page')

        reservas = paginator.get_page(page)

    return render(request, 'base.html', {'reservas': reservas})

# List

@login_required
def clientesList(request):

    search = request.GET.get('search')

    if search:

        clientes = Cliente.objects.filter(idPessoa__nome__contains=search)

    else:

        clientes_list = Cliente.objects.all().order_by('id')

        paginator = Paginator(clientes_list, 7)

        page = request.GET.get('page')

        clientes = paginator.get_page(page)

    return render(request, 'clientes/list.html', {'clientes': clientes})

@login_required
def dependenteList(request):

    search = request.GET.get('search')

    if search:

        dependentes = Dependente.objects.filter(nome__contains=search)

    else:

        dependentes_list = Dependente.objects.all().order_by('id')

        paginator = Paginator(dependentes_list, 7)

        page = request.GET.get('page')

        dependentes = paginator.get_page(page)

    return render(request, 'dependentes/list.html', {'dependentes': dependentes})

@login_required
def reservaList(request):

    search = request.GET.get('search')

    if search:

        reservas = Reserva.objects.filter(idCliente__idPessoa__nome__contains=search)

    else:
        
        # filto ordenado por data
        # now = timezone.now()        
        # reserva_list = Reserva.objects.filter(datareserva__gte=now).order_by('datareserva')

        reserva_list = Reserva.objects.all().order_by('id')

        paginator = Paginator(reserva_list, 7)

        page = request.GET.get('page')

        reservas = paginator.get_page(page)

    return render(request, 'reservas/list.html', {'reservas': reservas})

@login_required
def colaboradoresList(request):
    search = request.GET.get('search')

    if search:

        colaboradores = Colaborador.objects.filter(idPessoa__nome__contains=search)

    else:

        colaborador_list = Colaborador.objects.all().order_by('id')

        paginator = Paginator(colaborador_list, 7)

        page = request.GET.get('page')

        colaboradores = paginator.get_page(page)

    return render(request, 'colaboradores/list.html', {'colaboradores': colaboradores})

# View

@login_required
def clienteView(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, 'clientes/cliente.html', {'cliente': cliente})

@login_required
def reservaView(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    return render(request, 'reservas/reserva.html', {'reserva': reserva})

@login_required
def colaboradorView(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    return render(request, 'colaboradores/colaborador.html', {'colaborador': colaborador})

@login_required
def dependenteView(request, id):
    dependente = get_object_or_404(Dependente, pk=id)
    return render(request, 'dependentes/dependentes.html', {'dependente': dependente})

# Novo - Cadastrar

@login_required
def novaPessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST, request.FILES)

        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.save()
            #mensagem sucesso
            messages.info(request, 'Nova pessoa cadastrada com sucesso.')

            return redirect('/')
    else:
        form = PessoaForm()
        return render(request, 'addpessoa.html', {'form': form})

@login_required
def novoCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            cliente = form.save()
            
            messages.info(request, 'Cliente cadastrado com sucesso.')

            return redirect('/clientes/')
    else:
        form = ClienteForm()
        return render(request, 'clientes/addcliente.html', {'form': form})

@login_required
def novaReserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        search = request.GET.get('search')

        if search:

            reservas = Reserva.objects.filter(id__icontains=search)

        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.save()
            
            messages.info(request, 'Reserva cadastrada com sucesso.')

            return redirect('/reservas/')
    else:
        form = ReservaForm()
        return render(request, 'reservas/addreserva.html', {'form': form})

@login_required
def novoColaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)

        if form.is_valid():
            colaborador = form.save()
            
            messages.info(request, 'Colaborador cadastrado com sucesso.')

            return redirect('/colaboradores/')
    else:
        form = ColaboradorForm()
        return render(request, 'colaboradores/addcolaborador.html', {'form': form})
    
@login_required
def novoDependente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            cliente = form.save()
            
            messages.info(request, 'Cliente cadastrado com sucesso.')

            return redirect('/clientes/')
    else:
        form = DependenteForm()
        return render(request, 'dependentes/adddependentes.html', {'form': form})

# Editar

@login_required
def editarColaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = ColaboradorForm  (instance=colaborador)

    if(request.method == 'POST'):
        form = ColaboradorForm(request.POST, instance=colaborador)

        if(form.is_valid()):
            colaborador.save()
            
            messages.info(request, 'Colaborador editado com sucesso.')

            return redirect('/colaboradores/')
        else:
            return render(request, 'colaboradores/editarcolaborador.html', {'form': form})
    else:
        return render(request, 'colaboradores/editarcolaborador.html', {'form': form})

@login_required
def editarCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)

    if(request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)

        if(form.is_valid()):
            cliente.save()
            
            messages.info(request, 'Cliente editado com sucesso.')

            return redirect('/clientes/')
        else:
            return render(request, 'clientes/editarcliente.html', {'form': form})
    else:
        return render(request, 'clientes/editarcliente.html', {'form': form})

@login_required
def editarReserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    form = ReservaForm(instance=reserva)

    if(request.method == 'POST'):
        form = ReservaForm(request.POST, instance=reserva)

        if(form.is_valid()):
            reserva.save()
            
            messages.info(request, 'Reserva editada com sucesso.')

            return redirect('/reservas/')
        else:
            return render(request, 'reservas/editarreserva.html', {'form': form})
    else:
        return render(request, 'reservas/editarreserva.html', {'form': form})
    
@login_required
def editarDependente(request, id):
    dependente = get_object_or_404(Dependente, pk=id)
    form = DependenteForm(instance=dependente)

    if(request.method == 'POST'):
        form = DependenteForm(request.POST, instance=dependente)

        if(form.is_valid()):
            dependente.save()
            
            messages.info(request, 'Dependente editado com sucesso.')

            return redirect('/dependentes/')
        else:
            return render(request, 'dependentes/editardependentes.html', {'form': form})
    else:
        return render(request, 'dependentes/editardependentes.html', {'form': form})

# Deletar

@login_required
def deletarCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()

    messages.info(request, 'Cliente deletado com sucesso.')

    return redirect('/clientes/')

@login_required
def deletarColaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    colaborador.delete()

    messages.info(request, 'Colaborador deletado com sucesso.')

    return redirect('/colaboradores/')

@login_required
def deletarReserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    reserva.delete()

    messages.info(request, 'Reserva deletada com sucesso.')

    return redirect('/reservas/')

@login_required
def deletarDependente(request, id):
    dependente = get_object_or_404(Dependente, pk=id)
    dependente.delete()

    messages.info(request, 'Dependente deletado com sucesso.')

    return redirect('/dependentes/')