from django.shortcuts import render

def index(request):
	return render(request, 'main/index.html')

def about(request):
	return render(request, 'main/about.html')

def play(request):
	return render(request, 'main/play.html')

def tournaments(request):
	return render(request, 'main/tournaments.html')

def cards(request):
	return render(request, 'main/cards.html')