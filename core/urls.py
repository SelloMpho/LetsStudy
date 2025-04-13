from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect  # Correct import for redirect
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('home')),  # Redirect root URL to /home/
    path('home/', views.home, name='home'),
    path('assignments/', views.assignments, name='assignments'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('add-assignment/', views.add_assignment, name='add_assignment'),
]