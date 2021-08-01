from django import forms
from .models import User


# from django.core import validators

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','contact']
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'email': forms.EmailInput( attrs = {'class': 'form-control'}),
            'contact': forms.NumberInput( attrs = {'class': 'form-control'}),
        }