
from django import forms
from .models import Hall


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'
        widgets = {
            'location': forms.Textarea(attrs={'placeholder': 'Enter a short description of the hall location', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter the name of the hall' ,'class': 'form-control'}),
        }
        

    def __init__(self, *args, **kwargs):
        super(HallForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

            
