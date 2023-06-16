from django.urls import path
from . import views
from .forms import PlacesForm
from .views import PlacesDetailView


urlpatterns = [
	path('add', views.add, name='add_place'),
	path('<int:pk>', PlacesDetailView.as_view(), name='place_detail'),
	path(r'^delete/(?P<pk>\d+)/$', views.DeleteView.as_view(), name='delete_view_place'),
	path('edit/<int:pk>', views.edit, name='edit_view_place'),
]