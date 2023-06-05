from django.urls import path
from . import views
from .forms import PlacesForm
from .views import PlacesDetailView


urlpatterns = [
	path('add', views.add, name='add'),
	path('<int:pk>', PlacesDetailView.as_view(), name='place_detail'),
	#path('map', views.maps, name='maps')
]