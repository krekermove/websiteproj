from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea, Select

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'text','user', 'date', 'deadline']
        widgets = {
            'deadline':Select(attrs={
                'class': 'form-control'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст задачи'
            }),
        }
