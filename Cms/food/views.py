from django.shortcuts import render, redirect
from .forms import FoodForm, StoreForm
from .models import Store
from django.db.models import Case, When, Value, IntegerField
from django.utils import timezone

def dashboard(request):
    initial_date = request.session.get('date_added', None)
    initial_store = request.session.get('store', None)
    food_form = FoodForm(initial={'date_added': initial_date, 'store': initial_store})
    store_form = StoreForm()
    stores = Store.objects.all()
    return render(request, 'dashboard.html', {'food_form': food_form, 'store_form': store_form, 'stores': stores})

def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            # Uložení dat do session
            request.session['date_added'] = str(food.date_added)
            request.session['store'] = food.store.id
            return redirect('dashboard')
    else:
        # Načtení dat ze session
        initial_date = request.session.get('date_added', None)
        initial_store = request.session.get('store', None)
        form = FoodForm(initial={'date_added': initial_date, 'store': initial_store})
    return render(request, 'add_food.html', {'form': form})

def add_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.request = request
            form.save()
            return redirect('dashboard')
    else:
        form = StoreForm
    return render(request, 'add_food.html', {'form': form})
