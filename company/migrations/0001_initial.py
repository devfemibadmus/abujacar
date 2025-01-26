# Generated by Django 5.1.5 on 2025-01-26 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('intro', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='RX 350', max_length=10)),
                ('year', models.PositiveIntegerField(default=2010)),
                ('mileage', models.PositiveIntegerField(default=10000)),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('black', 'Black'), ('white', 'White'), ('silver', 'Silver'), ('green', 'Green'), ('yellow', 'Yellow'), ('grey', 'Grey'), ('orange', 'Orange'), ('brown', 'Brown')], default='black', max_length=20)),
                ('variant', models.CharField(choices=[('Standard', 'Standard'), ('Luxury', 'Luxury'), ('Sports', 'Sports'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid'), ('Diesel', 'Diesel')], default='Luxury', max_length=20)),
                ('type', models.CharField(choices=[('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Wagon', 'Wagon'), ('Van', 'Van'), ('Pickup', 'Pickup'), ('Minivan', 'Minivan'), ('Crossover', 'Crossover')], default='SUV', max_length=20)),
                ('condition', models.CharField(choices=[('NEW', 'Brand New'), ('USED', 'Used'), ('FOREIGN_USED', 'Foreign Used')], default='USED', max_length=20)),
                ('brand', models.CharField(choices=[('toyota', 'Toyota'), ('ford', 'Ford'), ('honda', 'Honda'), ('bmw', 'BMW'), ('audi', 'Audi'), ('mercedes_benz', 'Mercedes-Benz'), ('tesla', 'Tesla'), ('nissan', 'Nissan'), ('chevrolet', 'Chevrolet'), ('volkswagen', 'Volkswagen'), ('kia', 'Kia'), ('hyundai', 'Hyundai'), ('porsche', 'Porsche'), ('lexus', 'Lexus'), ('subaru', 'Subaru')], default='lexus', max_length=20)),
                ('preview_image', models.ImageField(upload_to='preview/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='FeaturePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post1', models.URLField(blank=True, null=True)),
                ('post2', models.URLField(blank=True, null=True)),
                ('post3', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiktok', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='company.car')),
            ],
            options={
                'verbose_name': 'car image',
                'verbose_name_plural': 'Car Images (Min 2, Max 15)',
            },
        ),
    ]
