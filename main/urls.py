from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('places', views.places, name='places')
]