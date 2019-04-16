import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm
)


def home(request):
    return render(request, 'core/index.html')


@login_required(login_url="home")
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


@login_required(login_url="home")
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required(login_url="home")
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)

@login_required(login_url="home")
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_pessoa_confirm.html', {'pessoa': pessoa})


@login_required(login_url="home")
def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


@login_required(login_url="home")
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required(login_url="home")
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required(login_url="home")
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_veiculos_confirm.html', {'veiculo': veiculo})


@login_required(login_url="home")
def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'form': form, 'mov_rot': mov_rot}
    return render(
        request, 'core/lista_movrotativos.html', data)
        

@login_required(login_url="home")
def movrotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


@login_required(login_url="home")
def movrotativos_update(request, id):
    data = {}
    movrotativos = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movrotativos)
    data['movrotativos'] = movrotativos
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativo.html', data)


@login_required(login_url="home")
def movrotativos_delete(request, id):
    movrotativos = MovRotativo.objects.get(id=id)
    
    if request.method == 'POST':
        movrotativos.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_movrotativos_confirm.html', {'movrotativos': movrotativos})


@login_required(login_url="home")
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'form': form, 'mensalistas': mensalistas}
    return render(
        request, 'core/lista_mensalistas.html', data)


@login_required(login_url="home")
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required(login_url="home")
def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalistas.html', data)


@login_required(login_url="home")
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_mensalistas_confirm.html', {'mensalista': mensalista})


@login_required(login_url="home")
def lista_movmensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'form': form, 'movmensalistas': movmensalistas}
    return render(
        request, 'core/lista_movmensalistas.html', data)


@login_required(login_url="home")
def movmensalistas_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


@login_required(login_url="home")
def movmensalistas_update(request, id):
    data = {}
    movmensalistas = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensalistas)
    data['movmensalistas'] = movmensalistas
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmensalistas.html', data)


@login_required(login_url="home")
def movmensalistas_delete(request, id):
    movmensalistas = MovMensalista.objects.get(id=id)
    
    if request.method == 'POST':
        movmensalistas.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_movmensalistas_confirm.html', {'movmensalistas': movmensalistas})

from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class pessoa_exporta_pdf(View):

        def get(self, request):
                pessoas = Pessoa.objects.all()
                params = {
                        'pessoas': pessoas,
                        'request': request,
                }
                return Render.render('core/relatorio_pessoa.html', params, 'relatorio_pessoas')


class pessoa_exporta_csv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio_pessoas.csv"'

        pessoas = Pessoa.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Nome', 'endereco', 'telefone'])

        for pessoa in pessoas:
            writer.writerow(
                [pessoa.id, pessoa.nome, pessoa.endereco, pessoa.telefone])

        return response


class veiculo_exporta_pdf(View):

        def get(self, request):
                veiculos = Veiculo.objects.all()
                params = {
                        'veiculos': veiculos,
                        'request': request,
                }
                return Render.render('core/relatorio_veiculo.html', params, 'relatorio_veiculos')


class veiculo_exporta_csv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio_veiculo.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])

        return response


class mensalista_exporta_pdf(View):

        def get(self, request):
                mensalistas = Mensalista.objects.all()
                params = {
                        'mensalistas': mensalistas,
                        'request': request,
                }
                return Render.render('core/relatorio_mensalista.html', params, 'relatorio_mensalista')


class mensalista_exporta_csv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio_mensalista.csv"'

        mensalistas = Mensalista.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Veiculo', 'Início', 'Valor Mes'])

        for mensalista in mensalistas:
            writer.writerow(
                [mensalista.id, mensalista.veiculo, mensalista.inicio, mensalista.valor_mes])

        return response


class movmensalista_exporta_pdf(View):

        def get(self, request):
                movmensalistas = MovMensalista.objects.all()
                params = {
                        'movmensalistas': movmensalistas,
                        'request': request,
                }
                return Render.render('core/relatorio_movmensalista.html', params, 'relatorio_movmensalista')


class movmensalista_exporta_csv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio_movmensalista.csv"'

        movmensalistas = MovMensalista.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Mensalista', 'Data Pagto.', 'Total'])

        for movmensalista in movmensalistas:
            writer.writerow(
                [movmensalista.id, movmensalista.mensalista, movmensalista.dt_pago,
                movmensalista.total])

        return response


class movrotativo_exporta_pdf(View):

        def get(self, request):
                movrotativos = MovRotativo.objects.all()
                params = {
                        'movrotativos': movrotativos,
                        'request': request,
                }
                return Render.render('core/relatorio_movrotativo.html', params, 'relatorio_movrotativo')


class movrotativo_exporta_csv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio_movrotativo.csv"'

        movrotativos = MovRotativo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Check-In', 'Check-Out', 'Valor/hora', 'Veiculo', 'Pago'])

        for movrotativo in movrotativos:
            writer.writerow(
                [movrotativo.id, movrotativo.checkin, movrotativo.checkout, movrotativo.valor_hora,
                 movrotativo.veiculo, movrotativo.pago
                 ])

        return response