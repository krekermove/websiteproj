from .models import Places
from django.forms import ModelForm, TextInput, Textarea, Select, CharField

class PlacesForm(ModelForm):
    class Meta:
        model = Places
        fields = ['title', 'text','user', 'date', 'deadline', 'lattitude', 'longtitude']
        widgets = {
            'deadline':Select(attrs={
                'class': 'form-control'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'lattitude':TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Широта'
            }),
            'longtitude': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Долгота'
            }),
        }
