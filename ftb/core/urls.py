from django.urls import path, include
from django.conf.urls import url

from ftb.core import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("federacao/", views.federacao, name="federacao"),
    path("noticias/", views.noticias, name="noticias"),
    path("noticias/<int:noticia_id>/", views.noticia_detalhes, name="noticia_detalhes"),
    path("eventos/", views.eventos, name="eventos"),
    path("eventos/<int:evento_id>/", views.evento_detalhes, name="evento_detalhes"),
    path("eventos/<int:evento_id>/inscricao", views.iframe, name="iframe"),
    path("contato/", views.contato, name="contato"),
    path("estatuto/", views.estatuto, name="estatuto"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
