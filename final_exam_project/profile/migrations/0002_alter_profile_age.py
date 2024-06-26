# Generated by Django 5.0.3 on 2024-04-07 14:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, help_text='Age requirement: 21 years and above.', null=True, validators=[django.core.validators.MinValueValidator(21)]),
        ),
    ]
