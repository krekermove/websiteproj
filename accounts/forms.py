from django.forms import ModelForm, TextInput, PasswordInput
from .models import Users

class UserForm(ModelForm):
	class Meta:
		model = Users
		fields = ['email', 'password']

		widgets = {
			"email": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Электронная почта'
				}),
			"password": PasswordInput(attrs={
				'class': 'form-control',
				'placeholder': 'Пароль'
				})
		}