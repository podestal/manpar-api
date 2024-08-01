# Generated by Django 5.0.7 on 2024-08-01 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_dish_dishimg_dishimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishimage',
            name='dish',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='api.dish'),
        ),
    ]
