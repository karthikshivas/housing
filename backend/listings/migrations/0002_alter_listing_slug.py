# Generated by Django 5.0 on 2023-12-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
