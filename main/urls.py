from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('about', views.about, name='about'),
	path('play', views.play, name='play'),
	path('tournaments', views.tournaments, name='tournaments'),
	path('cards', views.cards, name='cards')
]