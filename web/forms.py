from django import forms

class TripForm(forms.Form):
    current_location = forms.CharField(max_length=255, label='Current Location')
    destination = forms.CharField(max_length=255, label='Destination')
    budget = forms.DecimalField(max_digits=10, decimal_places=2, label='Budget')