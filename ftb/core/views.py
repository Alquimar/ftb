from django.shortcuts import render

def home(request):
    template_name = "home.html"
    context = {}
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
