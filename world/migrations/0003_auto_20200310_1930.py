# Generated by Django 3.0.4 on 2020-03-10 19:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_promotion_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='money',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='promotion',
            name='owner',
            field=models.CharField(default='Test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotion',
            name='size',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
