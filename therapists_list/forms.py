from .models import Therapists
from django.forms import ModelForm, TextInput, Textarea, FileInput

class TherapistForm(ModelForm):
    class Meta:
        model = Therapists
        fields = ['photo', 'firstname', 'lastname', 'phone',
                  'email', 'experience', 'degree',
                  'about', 'age', 'city', 'sex']

        widgets = {
            "photo": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Photo'
            }),
            "firstname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            "lastname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "experience": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Experience'
            }),
            "degree": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Education'
            }),
            "about": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'About therapists'
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age'
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
            "sex": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sex'
            })

        }
