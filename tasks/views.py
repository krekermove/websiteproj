import datetime

from django.shortcuts import render, redirect
from .forms import TasksForm
from .models import Tasks
from django.views.generic import DetailView

class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'tasks/task_detail.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.date = datetime.date.today()
            instance.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = TasksForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'tasks/createtask.html', data)
