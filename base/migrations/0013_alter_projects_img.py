# Generated by Django 4.2.6 on 2024-02-13 10:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_projects_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='img',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
