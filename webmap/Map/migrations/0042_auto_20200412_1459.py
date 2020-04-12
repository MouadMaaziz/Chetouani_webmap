# Generated by Django 2.2.5 on 2020-04-12 14:59

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0041_auto_20200404_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='Info_titre',
            field=models.CharField(default='A propos de Ste.Chetouani.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='about',
            name='Introduction',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='about',
            name='nos_Missions',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='about',
            name='nos_Valeurs',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='about',
            name='notre_Histoire',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='about',
            name='notre_Vision',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='about',
            name='qui_Somme_Nous',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='accueil_page',
            name='Intro',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='prestations_page',
            name='Description',
            field=models.TextField(max_length=1020),
        ),
    ]
