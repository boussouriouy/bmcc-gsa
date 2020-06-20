from django import forms
from .models import Member


class StudentForm(forms.ModelForm): 
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': ' preferred name'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'placeholder': 'optional'}))
    major = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'your major'}))
    term = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'your term'}))
    eboard = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'yes or No'}))
    alumni = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'yes or No'}))
    position = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'position or none'}))
    term = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'type term'}))
    class Meta:
        model = Member
        fields = [
            'image',
            'url',
            'name',
            'major',
            'eboard',
            'position',
            'alumni', 
            'term' 
        ]