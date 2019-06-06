from django.shortcuts import render

from .models import Noticia


def home(request):
    noticias_recentes = Noticia.objects.all().order_by('-criado_em')[:2]
    noticias_destaque = Noticia.objects.filter(destaque=True).order_by('criado_em')[:3]
    template_name = "core/home.html"
    context = {
        'noticias_recentes': noticias_recentes,
        'noticias_destaque': noticias_destaque
    }
    return render(request, template_name, context)


def federacao(request):
    template_name = "core/federacao.html"
    context = {}
    return render(request, template_name, context)


def noticias(request):
    noticias = Noticia.objects.all().order_by('-criado_em')
    template_name = "core/noticias.html"
    context = {
        'noticias': noticias
    }
    return render(request, template_name, context)


def eventos(request):
    template_name = "core/eventos.html"
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
