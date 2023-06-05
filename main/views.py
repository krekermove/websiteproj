from django.shortcuts import render
import sys
sys.path.append("..")
from tasks.models import Tasks
from places.models import Places

def index(request):
	tasks = Tasks.objects.all()
	return render(request, 'main/index.html', {'tasks': tasks})
def places(request):
	places = Places.objects.all()
	return render(request, 'main/places.html', {'places': places})

def casino(request):
	return render(request, 'main/casino.html')