# Generated by Django 5.0.6 on 2024-06-13 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_remove_continet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='continet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
