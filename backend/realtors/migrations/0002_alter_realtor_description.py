# Generated by Django 5.0 on 2023-12-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
