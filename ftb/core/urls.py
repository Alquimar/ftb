from django.urls import path

from ftb.core import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("federacao/", views.federacao, name="federacao"),
    path("noticias/", views.noticias, name="noticias"),
    path("noticias/<int:noticia_id>/", views.noticia_detalhes, name="noticia_detalhes"),
    path("eventos/", views.eventos, name="eventos"),
    path("eventos/<int:evento_id>/", views.evento_detalhes, name="evento_detalhes"),
    path("contato/", views.contato, name="contato"),
    path("estatuto/", views.estatuto, name="estatuto"),
    # path("federacao/", views.federacao, name="federacao"),
]
