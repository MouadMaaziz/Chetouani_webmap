# Generated by Django 2.2.5 on 2020-04-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0044_auto_20200412_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Titre_carte',
            field=models.CharField(default='ou sommes nou aujourdhui', max_length=300),
        ),
    ]
