from django.shortcuts import render, redirect
from core.forms import FormCliente, FormFabricante, FormVeiculo
from core.models import Cliente, Veiculo, Fabricante
# Create your views here.

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'


@login_required
def cadastro_Cliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_clientes')
    contexto = {'form': form, "label_botao":"cadastrar"}
    return render(request, 'cadastro_cliente.html', contexto)


def cadastro_Veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_veiculos')
    contexto = {'form': form}
    return render(request, 'cadastro_veiculo.html', contexto)


def cadastro_Fabricante(request):
    form = FormFabricante(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_fabricantes')
    contexto = {'form': form}
    return render(request, 'cadastro_fabricante.html', contexto)


@login_required
def listagem_clientes(request):
    dados = Cliente.objects.all()
    if request.POST and request.POST["pesquisar"]:
        dados = Cliente.objects.filter(nome__icontains=request.POST["pesquisar"])
    contexto = {'dados': dados}
    return render(request, 'listagem_clientes.html', contexto)


def listagem_veiculos(request):
    dados = Veiculo.objects.all()
    if request.POST and request.POST["pesquisar"]:
        dados = Veiculo.objects.filter(nome__icontains=request.POST["pesquisar"])
    contexto = {'dados': dados}
    return render(request, 'listagem_veiculos.html', contexto)


def listagem_fabricantes(request):
    dados = Fabricante.objects.all()
    if request.POST and request.POST["pesquisar"]:
        dados = Fabricante.objects.filter(nome__icontains=request.POST["pesquisar"])
    contexto = {'dados': dados}
    return render(request, 'listagem_fabricantes.html', contexto)


def atualiza_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("url_listagem_clientes")
    contexto = {'form': form, 'label_botao': 'Atualizar', 'titulo_h1': 'Atualização de cliente'}
    return render(request, 'cadastro_cliente.html', contexto)


def exclui_cliente(request, id):
    obj = Cliente.objects.get(id = id)
    if request.POST:
        obj.delete()
        return redirect("url_listagem_clientes")
    contexto = {'tipo_confirmacao': 'cliente', 'valor_confirmacao': obj.nome}
    return render(request, 'confirmacao.html', contexto)

