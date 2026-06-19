from django import forms
from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car

        fields = [
            'owner_name',
            'phone',
            'car_type',
            'car_color',
            'plate_number',
            'notes'
        ]

        widgets = {
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'car_type': forms.TextInput(attrs={'class': 'form-control'}),
            'car_color': forms.TextInput(attrs={'class': 'form-control'}),
            'plate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }