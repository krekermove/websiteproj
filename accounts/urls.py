from django.urls import path, include
from .views import Register, Profile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('profile/', Profile.as_view(), name='profile')
]