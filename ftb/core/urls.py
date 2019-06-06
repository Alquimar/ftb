from django.urls import path

from ftb.core import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("federacao/", views.federacao, name="federacao"),
    path("noticias/", views.noticias, name="noticias"),
    path("eventos/", views.eventos, name="eventos"),
    path("contato/", views.contato, name="contato"),
    path("estatuto/", views.estatuto, name="estatuto"),
    # path("federacao/", views.federacao, name="federacao"),
]
