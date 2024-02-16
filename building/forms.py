
from django import forms
from .models import Hall


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'Enter a short description of the hall location'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter the name of the hall'}),
        }
        

    def __init__(self, *args, **kwargs):
        super(HallForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

            
