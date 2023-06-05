from . import views
from django.urls import path


urlpatterns = [
	path('', views.index, name='home'),
	path('places', views.places, name='places'),
	path('casino', views.casino, name='casino'),
]