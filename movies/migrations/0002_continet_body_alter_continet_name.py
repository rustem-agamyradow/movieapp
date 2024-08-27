# Generated by Django 5.0.6 on 2024-06-06 08:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='continet',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='continet',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
