# Generated by Django 2.2.5 on 2020-04-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0042_auto_20200412_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='de_nous',
            field=models.CharField(default='qui somme nous ?', max_length=300),
        ),
        migrations.AddField(
            model_name='about',
            name='histoire',
            field=models.CharField(default='voila notre histoire', max_length=300),
        ),
        migrations.AddField(
            model_name='about',
            name='missions',
            field=models.CharField(default='nos missions', max_length=300),
        ),
        migrations.AddField(
            model_name='about',
            name='valeurs',
            field=models.CharField(default='nos valeurs', max_length=300),
        ),
        migrations.AddField(
            model_name='about',
            name='vision',
            field=models.CharField(default='notre vision', max_length=300),
        ),
    ]
