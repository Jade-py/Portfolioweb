# Generated by Django 4.2.6 on 2023-11-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_skills_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='icon',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
