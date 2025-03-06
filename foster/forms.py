from django import forms
from .models import FosterRequest, Pet, FosterFamily

class FosterRequestForm(forms.ModelForm):
    class Meta:
        model = FosterRequest
        fields = ['pet', 'foster_family']

    foster_family = forms.ModelChoiceField(queryset=FosterFamily.objects.all(), required=True)

class FosterFamilyForm(forms.ModelForm):
    class Meta:
        model = FosterFamily
        fields = ['name', 'address', 'email', 'phone_number', 'number_of_pets']

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'health_status', 'special_needs', 'date_taken_in']