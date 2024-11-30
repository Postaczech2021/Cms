from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Outcome(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    PAYMENT_CHOICES = [
        ('CARD', 'Platební Karta'),
        ('PLUXEE', 'Pluxee karta'),
        ('CASH', 'Hotovost'),
    ]

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.get_method_display()

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
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    date_added = models.DateField(default=timezone.now)
    quantity = models.FloatField(default=1)
    unit = models.CharField(max_length=10, choices=UNITS)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,default=1)
    note = models.TextField(blank=True, null=True)





