from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        labels = {
            'laptop_id':'LAPTOP ID',
            'model_name':'MODEL',
            'brand':'BRAND',
            'ram':'RAM',
            'processor':'PROCESSOR',
            'price':'PRICE'
        }
        widgets = {
            'laptop_id':forms.NumberInput(attrs={'class':'form-control'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'ram': forms.NumberInput(attrs={'class': 'form-control'}),
            'processor': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
