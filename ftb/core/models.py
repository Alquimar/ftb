from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from model_utils import Choices
from ckeditor.fields import RichTextField


class AbstractModel(models.Model):
    titulo = models.CharField('Título', max_length=100)
    descricao = RichTextField('Descrição', blank=True, null=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Noticia(AbstractModel):
    imagem = models.ImageField(upload_to='notiticas/imagens', verbose_name='Imagem',
                               null=True, blank=True)
    ordem = models.IntegerField('Ordem', null=True, blank=True)
    destaque = models.BooleanField('Em destaque?', default=False)

    def __str__(self):
        return '{}'.format(self.titulo)

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'


class Evento(AbstractModel):
    TIPO_EVENTO_COMPETICAO = 10
    TIPO_EVENTO_CURSO = 20

    tipo_evento_choices = Choices(
        (TIPO_EVENTO_COMPETICAO, 'Competição'),
        (TIPO_EVENTO_CURSO, 'Curso')
    )

    tipo_evento = models.IntegerField('Tipo', choices=tipo_evento_choices)
    imagem = models.ImageField(upload_to='eventos/imagens', verbose_name='Imagem',
                               null=True, blank=True)
    data_inicio = models.DateField('Início')
    data_fim = models.DateField('Fim')
    inscricao_data_inicio = models.DateField('Início das inscrições')
    inscricao_data_fim = models.DateField('Fim das inscrições')
    inscricao_formulario = models.CharField('Formulário', max_length=1000)
    # pdf = models.FileField(upload_to='eventos/pdfs', verbose_name='Regulamento/Normas')


@receiver(post_delete, sender=Evento)
@receiver(post_delete, sender=Noticia)
def submission_delete(sender, instance, **kwargs):
    instance.imagem.delete(False)
    # if sender.__name__ == "Evento":
    #     instance.pdf.delete(False)
