from django.db import models


class AbstractModel(models.Model):
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Noticia(AbstractModel):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição')
    imagem = models.ImageField(upload_to='notiticas/imagens', verbose_name='Imagem',
                               null=True, blank=True)
    ordem = models.IntegerField('Ordem', null=True, blank=True)
    destaque = models.BooleanField('Em destaque?', default=False)

    def __str__(self):
        return '{}'.format(self.titulo)

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
