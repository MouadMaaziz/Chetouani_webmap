# Generated by Django 2.2.5 on 2020-03-31 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0016_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Icon',
            field=models.CharField(default='fas fa-', max_length=50),
        ),
    ]
