from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']  # Use a list, not a set
    
    widgets = {
        "category": forms.Select(attrs={
            'class': 'w-full py-4 rounded-xl border'
        }),
        "name": forms.TextInput(attrs={
            'class': 'w-full py-4 rounded-xl border'
        }),
        "description": forms.Textarea(attrs={
            'class': 'w-full py-4 rounded-xl border',
            'rows': 2
        }),
        "price": forms.NumberInput(attrs={
            'class': 'w-full py-4 rounded-xl border'
        }),
        "image": forms.ClearableFileInput(attrs={
            'class': 'w-full py-4 rounded-xl border'
        }),
    }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'is_sold']  # Use a list, not a set
    
    widgets = {
        
        "name": forms.TextInput(attrs={
            'class': 'w-full py-4 rounded-xl border'
        }),
        "description": forms.Textarea(attrs={
            'class': 'w-full py-4 rounded-xl border',
            'rows': 2
        }),
        "price": forms.NumberInput(attrs={
            'class': 'w-full py-4 rounded-xl border'
        }),
        "image": forms.ClearableFileInput(attrs={
            'class': 'w-full py-4 rounded-xl border'
        }),
    }

