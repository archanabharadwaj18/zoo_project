"""
URL configuration for zoo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Home page
    path('', views.display_home, name='home'),

    # Hardcoded animals
    path('tiger/', views.display_tiger, name='tiger'),
    path('lion/', views.display_lion, name='lion'),
    path('monkey/', views.display_monkey, name='monkey'),
    path('snakes/', views.display_snake, name='snakes'),
    path('birds/', views.display_bird, name='birds'),

    # Database animals
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<str:aid>/', views.animal_detail, name='animal_detail'),
]
