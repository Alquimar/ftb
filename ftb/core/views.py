from django.shortcuts import render

from .models import Noticia, Evento


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


def noticia_detalhes(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id)
    template_name = "core/artigo.html"
    context = {
        'artigo': noticia
    }
    return render(request, template_name, context)


def eventos(request):
    cursos = Evento.objects.filter(tipo_evento=Evento.TIPO_EVENTO_CURSO)
    competicoes = Evento.objects.filter(tipo_evento=Evento.TIPO_EVENTO_COMPETICAO)
    template_name = "core/eventos.html"
    context = {
        'cursos': cursos,
        'competicoes': competicoes
    }
    return render(request, template_name, context)


def evento_detalhes(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    template_name = "core/artigo.html"
    context = {
        'artigo': evento
    }
    return render(request, template_name, context)


def contato(request):
    template_name = "core/contato.html"
    context = {}
    return render(request, template_name, context)


def estatuto(request):
    template_name = "core/estatuto.html"
    context = {}
    return render(request, template_name, context)


def iframe(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    template_name = "core/inscricao.html"
    context = {
        'evento': evento
    }
    return render(request, template_name, context)
