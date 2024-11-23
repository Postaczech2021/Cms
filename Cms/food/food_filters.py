from django.shortcuts import render
from .models import Food

def filter_by_category(request, category_id):
    print(f"Filtering by category_id: {category_id}")
    foods = Food.objects.filter(food_type_id=category_id)
    print(f"QuerySet: {foods}")
    return render(request, 'food_list.html', {'foods': foods})
