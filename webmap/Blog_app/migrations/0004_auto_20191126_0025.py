# Generated by Django 2.2.5 on 2019-11-26 00:25

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0003_auto_20191125_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='Contenu',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
