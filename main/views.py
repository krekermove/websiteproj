from django.shortcuts import render

def index(request):
	return render(request, 'main/index.html')

def places(request):
	return render(request, 'main/places.html')

def casino(request):
	return render(request, 'main/casino.html')