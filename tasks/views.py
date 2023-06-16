import datetime

from django.shortcuts import render, redirect
from .forms import TasksForm
from .models import Tasks
from django.views.generic import DetailView, DeleteView

class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'tasks/task_detail.html'

class DeleteView(DeleteView):
    model = Tasks
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        return super(DeleteView, self).delete(request, *args, **kwargs)

def edit(request, pk):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        error = ''
        if form.is_valid():
            instance = form.save(commit=False)
            Tasks.objects.filter(id=pk).update(
                title=instance.title,
                text=instance.text,
                date=datetime.date.today(),
                deadline=instance.deadline
            )
            return redirect('home')
        else:
            error = 'Ошибка заполнения'

    obj = Tasks.objects.get(id=pk)
    form = TasksForm(instance=obj)
    context = {
        'form': form
    }
    return render(request, 'tasks/editpage.html', context)

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
