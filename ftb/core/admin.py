from django.contrib import admin

from .models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'ordem', 'imagem']
    search_fields = ['titulo']
    list_filter = ['ordem', 'criado_em']


admin.site.register(Noticia, NoticiaAdmin)
