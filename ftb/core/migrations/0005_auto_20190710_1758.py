# Generated by Django 2.2.1 on 2019-07-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_evento_tipo_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='pdf',
            field=models.FileField(upload_to='eventos/pdfs', verbose_name='Regulamento/Normas'),
        ),
    ]