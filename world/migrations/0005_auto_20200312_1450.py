# Generated by Django 3.0.4 on 2020-03-12 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='won_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='world.Wrestler'),
        ),
    ]
