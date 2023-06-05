from django.urls import path
from . import views

urlpatterns = [
	path('', views.vinnik, name='casino'),
	path('door/', views.vinnik, name='door'),
	path('run/', views.vasykov, name='run')
]