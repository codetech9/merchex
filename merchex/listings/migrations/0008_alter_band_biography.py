# Generated by Django 4.0.5 on 2022-06-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_listing_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='biography',
            field=models.CharField(max_length=1000),
        ),
    ]
