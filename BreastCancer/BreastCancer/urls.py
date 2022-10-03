"""TextUtils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import veiws

urlpatterns = [
    path('', veiws.post_data, name='base'),
    path('admin/', admin.site.urls, name="admin"),
    path('home', veiws.display_one, name="home"), 
    path('facebook', veiws.get_facebook, name="facebook"), 
    path('google', veiws.get_google, name="google"), 
    path('pornhub', veiws.watch_porn, name="porn"), 
    path('back', veiws.back, name="back")
]
