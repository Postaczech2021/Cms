from django.db.models import Case, When, Value, IntegerField
from django import forms
from .models import Food, Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': "Název obchodu"
        }

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'quantity', 'unit', 'store', 'date_added', 'note']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
            'date_added': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'note': forms.Textarea(attrs={'class': 'form-control','rows': 5}),
        }
        labels = {
            'name': "Název položky",
            'quantity': "Množství",
            'unit': "Jednotky",
            'store': "Obchod",
            'date_added': "Datum přidání",
            'note': "Poznámka"
        }

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.fields['store'].queryset = Store.objects.exclude(name="Undefined").order_by('name')
