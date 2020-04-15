# Generated by Django 2.2.5 on 2020-04-14 23:47

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0051_auto_20200414_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestations_page',
            old_name='Contenu',
            new_name='Introduction',
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='par1',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='par2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='par3',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='par4',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='par5',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='par6',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='sous_titre1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='sous_titre2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='sous_titre3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='sous_titre4',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='sous_titre5',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='prestations_page',
            name='sous_titre6',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
