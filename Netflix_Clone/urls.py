"""
URL configuration for Netflix_Clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/',home,name='home'),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('base/',base,name='base'),
    path('main_page/',main_page,name='main_page'),
    path('tvshows/',tvshows,name='tvshows'),
    path('movies/',movies,name='movies'),
    path('new_popular/',new_popular,name='new_popular'),
    path('children/',children,name='children'),
    path('profile/',profile,name='profile'),
    path('user_logout/',user_logout,name='user_logout'),
    path('change_password/',change_password,name='change_password'),
    path('reset_password/',reset_password,name='reset_password'),
]
