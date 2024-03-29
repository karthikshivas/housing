# Generated by Django 5.0 on 2023-12-20 13:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0002_alter_realtor_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True)),
                ('sale_type', models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='For Sale', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('home_type', models.CharField(choices=[('House', 'House'), ('Condo', 'Condo'), ('Town House', 'Townhouse')], default='House', max_length=150)),
                ('sqft', models.IntegerField()),
                ('open_house', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('realtor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='listings', to='realtors.realtor')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='listing_photos/')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='listings.listing')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='main_photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_photo_listing', to='listings.photo'),
        ),
    ]
