from django.shortcuts import render, redirect, get_object_or_404
from .forms import FoodForm, StoreForm
from .models import Store, Food, FoodType
from django.db.models import Case, When, Value, IntegerField
from django.utils import timezone

def dashboard(request):

    foods = Food.objects.select_related('store').all()

    initial_date = request.session.get('date_added', None)
    initial_store = request.session.get('store', None)
    food_form = FoodForm(initial={'date_added': initial_date, 'store': initial_store})
    store_form = StoreForm()
    stores = Store.objects.all()
    return render(request, 'dashboard.html', {'food_form': food_form, 'store_form': store_form, 'stores': stores,'foods': foods})

def delete_store(request,id):
    store = get_object_or_404(Store, pk=id)
    store.delete()
    return redirect('dashboard')


def edit_store(request, id):
    store = get_object_or_404(Store, id=id)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form = StoreForm(instance=store)
            # If the form is not valid, render the form again with error messages
            return render(request, 'edit_store.html', {'form': form, 'store': store})
    else:
        form = StoreForm(instance=store)
        return render(request, 'edit_store.html', {'form': form, 'store': store})

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