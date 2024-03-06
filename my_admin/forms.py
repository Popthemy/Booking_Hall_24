from django import forms
from .models import DefaultRepList




class RepListForm(forms.ModelForm):
    
    class Meta:
        model = DefaultRepList
        fields = ['first_name', "last_name", "email"]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name as on your course form...', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name as on your course form...', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address...', 'class': 'form-control'}),
        }