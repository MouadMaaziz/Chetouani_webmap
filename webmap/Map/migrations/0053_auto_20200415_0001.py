# Generated by Django 2.2.5 on 2020-04-15 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0052_auto_20200414_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestations_page',
            name='sous_titre1',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='prestations_page',
            name='sous_titre2',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='prestations_page',
            name='sous_titre3',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='prestations_page',
            name='sous_titre4',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='prestations_page',
            name='sous_titre5',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='prestations_page',
            name='sous_titre6',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
