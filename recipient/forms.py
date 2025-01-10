# recipient/forms.py
from django import forms
from .models import Recipient

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'age', 'organ_needed', 'blood_group', 'location', 'mobile_number']
