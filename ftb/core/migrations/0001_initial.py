# Generated by Django 2.2.1 on 2019-06-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='notiticas/imagens', verbose_name='Imagem')),
                ('ordem', models.IntegerField(blank=True, null=True, verbose_name='Ordem')),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
    ]
