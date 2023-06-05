from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('activate/<slug:uidb64>/<slug:token>', views.activate, name='activate'),
    path('login/', views.Login.as_view(template_name='login.html'), name='login')
]