# Generated by Django 2.2.5 on 2020-03-27 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0013_auto_20200326_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projet',
            old_name='link',
            new_name='link_à_supprimer',
        ),
    ]
