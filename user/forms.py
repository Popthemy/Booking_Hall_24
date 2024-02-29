from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django import forms
from .models import RepProfile

class RepCustomUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username',
                  'password1', 'password2',]  # '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name as on your course form...', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name as on your course form...', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username...', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address...', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(RepCustomUserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'password1':
                field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your password'})
            if  name == 'password2':
                field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm your password'})


class RepProfileForm(forms.ModelForm):
    class Meta:
        model = RepProfile
        fields = ['first_name', 'last_name', 'email','username', 'level','contact_info', 'bio' , 'i_am_a_rep'] 
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name as on your course form...', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name as on your course form...', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username...', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address...', 'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Enter your department and other other details...', 'class': 'form-control'}),
            'i_am_a_rep': forms.CheckboxInput(attrs={ 'class': 'boolean-field'}),
        }

    def __init__(self, *args, **kwargs):
        super(RepProfileForm,self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != 'i_am_a_rep':
                field.widget.attrs.update({'class':'form-control'})
