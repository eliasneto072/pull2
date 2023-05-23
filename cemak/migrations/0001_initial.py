# Generated by Django 4.2.1 on 2023-05-23 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10, verbose_name='Nome banner')),
                ('posicao', models.CharField(blank=True, choices=[('4', '1'), ('3', '2'), ('2', '3'), ('1', '4')], max_length=1, null=True, unique=True, verbose_name='')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='Banner', verbose_name='Banner')),
            ],
            options={
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('localizacao', models.CharField(max_length=100, verbose_name='localização')),
                ('contato', models.IntegerField(default=' +55 (00) 9', verbose_name='Contato')),
                ('saiba_mais', models.CharField(max_length=100, verbose_name='Saiba mais')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manchete', models.CharField(max_length=200)),
                ('materia', models.CharField(max_length=1000)),
                ('autor', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Vídeo',
                'verbose_name_plural': 'Vídeos',
            },
        ),
    ]