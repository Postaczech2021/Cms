import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('date_added', models.DateField()),
                ('quantity', models.FloatField()),
                ('unit', models.CharField(choices=[('pieces', 'ks'), ('grams', 'g'), ('mililiters', 'ml'), ('liters', 'l')], max_length=10)),
                ('note', models.TextField(blank=True, null=True)),
                ('food_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='food.foodtype')),
                ('store', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='food.store')),
            ],
        ),
    ]
