# Generated by Django 5.1.2 on 2024-11-25 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodtype'),
        ),
        migrations.AlterField(
            model_name='food',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.paymentmethod'),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.store'),
        ),
    ]
