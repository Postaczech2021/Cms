from django.db import models
from django.utils import timezone

class Store(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FoodType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Food(models.Model):
    UNITS = [
        ('pieces', 'ks'),
        ('grams', 'g'),
        ('mililiters', 'ml'),
        ('liters','l')
    ]

    name = models.CharField(max_length=255)
    food_type = models.ForeignKey(FoodType, related_name='foods' ,on_delete=models.CASCADE, default=1)
    price = models.FloatField()
    date_added = models.DateField(default=timezone.now)
    quantity = models.FloatField(default=1)
    unit = models.CharField(max_length=10, choices=UNITS)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,default=1)
    note = models.TextField(blank=True, null=True)

