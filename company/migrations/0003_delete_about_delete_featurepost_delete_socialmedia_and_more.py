# Generated by Django 5.1.5 on 2025-01-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_car_posturl_alter_car_brand_alter_car_color_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='FeaturePost',
        ),
        migrations.DeleteModel(
            name='SocialMedia',
        ),
        migrations.AddField(
            model_name='car',
            name='amount',
            field=models.PositiveIntegerField(default=10000000),
        ),
    ]
