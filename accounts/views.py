from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Users 

def accounts(request):
	return render(request, 'accounts/accounts.html')

def register(request):
	error = ''
	form = UserForm()
	if request.method=='POST':
		form = UserForm(request.POST)
		if form.is_valid():
			if Users.objects.filter(email=form.cleaned_data.get("email")):
				error = 'Такой пользователь уже существует'
			else:
				form.save()
				return redirect('accounts')
		else:
			error = 'Ошибка'

	data = {
		'form': form,
		'error': error
	}
	return render(request, 'accounts/register.html', data)

def login(request):
	error = ''
	form = UserForm()

	if request.method=='POST':
		form = UserForm(request.POST)
		if form.is_valid():
			if Users.objects.filter(email=form.cleaned_data.get("email")).filter(password=form.cleaned_data.get("password")):
				return redirect('accounts')
			else:
				if form.cleaned_data.get("email") not in Users.objects.all():
					error = 'Пользователь не найден или пароль не верный'
		else:
			error = 'Ошибка'
	data = {
		'form': form,
		'error': error
	}

	return render(request, 'accounts/login.html', data)