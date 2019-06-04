from django.shortcuts import render

from .models import Noticia

def home(request):
    noticias = Noticia.objects.all()
    template_name = "core/home.html"
    context = {
        'noticias': noticias
    }
    return render(request, template_name, context)


def federacao(request):
    template_name = "core/federacao.html"
    context = {}
    return render(request, template_name, context)


def competicoes(request):
    template_name = "core/competicoes.html"
    context = {}
    return render(request, template_name, context)


def contato(request):
    template_name = "core/contato.html"
    context = {}
    return render(request, template_name, context)


def estatuto(request):
    template_name = "core/estatuto.html"
    context = {}
    return render(request, template_name, context)
