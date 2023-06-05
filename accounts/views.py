from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm
import sys
sys.path.append("..")
from tasks.models import Tasks

class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        error = ''
        if form.is_valid():
            email = str(form.cleaned_data.get('email'))
            if "@voenmeh.ru" in email:
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')
            else:
                error = 'Используйте почту вида: name@voenmeh.ru'
        context = {
            'form': form,
            'error': error
        }
        return render(request, self.template_name, context)

class Profile(View):

    template_name = 'accounts/profile.html'

    def get(self, request):
        username = request.user
        task = Tasks.objects.all().filter(user=username)
        context = {
            'tasks': task,
        }
        return render(request, self.template_name, context)