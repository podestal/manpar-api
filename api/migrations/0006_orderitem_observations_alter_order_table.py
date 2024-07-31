# Generated by Django 5.0.7 on 2024-07-31 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_order_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='observations',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.table'),
        ),
    ]
