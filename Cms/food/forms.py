from django import forms
from .models import Food, Store, FoodType, PaymentMethod
from django.utils import timezone
#Storeform
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Název obchodu',
        }

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'food_type', 'price', 'quantity','unit', 'date_added', 'store', 'payment_method','note']
        labels = {
            'name': 'Název',
            'food_type': 'Typ potraviny',
            'price': 'Cena',
            'quantity': 'Množství',
            'unit':'Jednotky',
            'date_added': 'Datum přidání',
            'store': 'Obchod',
            'payment_method': 'Způsob platby',
            'note':'Poznámka',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'food_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control','step':'0.01'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'date_added': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'note':forms.Textarea(attrs={'rows':4,'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].initial = 0.0
        self.fields['date_added'].initial = timezone.now()
        self.fields['food_type'].queryset = FoodType.objects.all()
        self.fields['store'].queryset = Store.objects.all()
        self.fields['payment_method'].choices = [(pm.id, pm.name) for pm in PaymentMethod.objects.all()]
