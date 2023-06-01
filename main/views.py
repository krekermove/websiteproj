from django.shortcuts import render
import sys
sys.path.append("..")
from tasks.models import Tasks

def index(request):
	tasks = Tasks.objects.all()
	return render(request, 'main/index.html', {'tasks': tasks})

def places(request):
	return render(request, 'main/places.html')

def casino(request):
	return render(request, 'main/casino.html')