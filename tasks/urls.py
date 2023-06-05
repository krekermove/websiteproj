from django.urls import path
from . import views
from .forms import TasksForm
from .views import TaskDetailView


urlpatterns = [
	path('create', views.create, name='create'),
	path('<int:pk>', TaskDetailView.as_view(), name='task_detail'),
	path(r'^delete/(?P<pk>\d+)/$', views.DeleteView.as_view(), name='delete_view_task'),
	path('edit/<int:pk>', views.edit, name='edit_view'),
]