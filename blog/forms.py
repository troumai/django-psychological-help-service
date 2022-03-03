from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput

from blog.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article Text'
            }),
            "picture": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a picture'
            }),
        }