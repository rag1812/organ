from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            'name', 
            'age', 
            'blood_group', 
            'organ', 
            'location', 
            'mobile_number', 
            'is_deceased', 
            'hiv_status', 
            'willing_to_donate',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'organ': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mobile number'}),
            'is_deceased': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'hiv_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'willing_to_donate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
