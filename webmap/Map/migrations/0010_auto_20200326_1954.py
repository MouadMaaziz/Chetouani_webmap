# Generated by Django 2.2.5 on 2020-03-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0009_auto_20200326_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='Type',
        ),
        migrations.AddField(
            model_name='projet',
            name='Département',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AddField(
            model_name='projet',
            name='Services',
            field=models.CharField(choices=[('Public', 'Public'), ('Privé', 'Privé')], default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='projet',
            name='Tel',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='projet',
            name='Adress',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
