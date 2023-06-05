from django.shortcuts import render


def lobby(request):
    return render(request, 'casino/casino.html')

def vinnik(request):
    return render(request, 'casino/door.html')

def vasykov(request):
    return render(request, 'casino/casino.html')
