from django.shortcuts import render
from .models import Contato, HomePage, ServicoPage, SobrePage, PlanosPage

def home(request):
    data = HomePage.objects.get(id=1)
    return render(request, 'website/index.html', {
        'linha1coluna1': data.linha1coluna1,
        'linha1coluna2': data.linha1coluna2,

        'linha2coluna1': data.linha2coluna1,
        'linha2coluna2': data.linha2coluna2,

        'linha3coluna1': data.linha3coluna1,
        'linha3coluna2': data.linha3coluna2
        })

def contato(request):
    #import pdb; pdb.set_trace()
    mensagem = ''
    if request.method == 'POST':
        try:
            contato = {}
            contato['nome'] = request.POST.get('nome')
            contato['email'] = request.POST.get('email')
            contato['telefone'] = request.POST.get('telefone')
            contato['mensagem'] = request.POST.get('mensagem')

            Contato.objects.create(**contato)
        
        except Exception as e:
            mensagem = str(e)
        else:
            mensagem = 'Contato realizado com sucesso'
    
    return render(request, 'website/contato.html', {'mensagem': mensagem})

def servicos(request):
    data = ServicoPage.objects.get(id=1)
    return render(request, 'website/servicos.html', {'textounico': data.textounico})

def sobre(request):
    data = SobrePage.objects.get(id=1)
    return render(request, 'website/sobre.html', {'linha1': data.linha1, 'linha2': data.linha2})

def planos(request):
    data = PlanosPage.objects.get(id=1)
    return render(request, 'website/planos.html', {'linha1': data.linha1, 'linha2': data.linha2})