from django.forms import  ModelForm, TextInput
from django import forms
from .models import Todo

class AddForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('name', 'category')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }