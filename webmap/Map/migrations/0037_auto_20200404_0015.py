# Generated by Django 2.2.5 on 2020-04-04 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0036_about_info_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accueil_page',
            name='actualite_section',
            field=models.CharField(default='Nos actualites', max_length=200),
        ),
        migrations.AlterField(
            model_name='accueil_page',
            name='prestations_section',
            field=models.CharField(default='Nos prestations du service', max_length=200),
        ),
        migrations.AlterField(
            model_name='accueil_page',
            name='video_phrase1',
            field=models.CharField(default='WE ARE HERE TO CREATE A LASTING RELATIONSHIP WITH YOU', max_length=200),
        ),
        migrations.AlterField(
            model_name='accueil_page',
            name='video_phrase2',
            field=models.CharField(default='GEOMATIQUE- AMENAGEMENT- EXPERTISE FINANCIER', max_length=200),
        ),
        migrations.AlterField(
            model_name='accueil_page',
            name='video_titre',
            field=models.CharField(default='STE CHETOUANI TOPOGRAPHIE & GEOMATIQUE', max_length=200),
        ),
    ]