# Generated by Django 2.2.5 on 2020-04-14 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0049_about_nos_partenaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accueil', models.CharField(blank=True, default='Accueil', max_length=80, null=True)),
                ('Contact', models.CharField(blank=True, default='Contact', max_length=80, null=True)),
                ('A_propos', models.CharField(blank=True, default='Accueil', max_length=80, null=True)),
                ('Prestations', models.CharField(blank=True, default='A_propos', max_length=80, null=True)),
                ('Actualite', models.CharField(blank=True, default='Actualite', max_length=80, null=True)),
            ],
        ),
    ]
