from django.contrib import admin

from .models import Noticia, Evento


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'ordem', 'imagem']
    search_fields = ['titulo']
    list_filter = ['ordem', 'criado_em']


class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'data_inicio', 'data_fim']
    search_fields = ['titulo']
    list_filter = ['criado_em', 'data_inicio']


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Evento, EventoAdmin)
