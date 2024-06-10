from django.urls import path
from . import views
from django.contrib import admin

# http://127.0.0.1:8000/

urlpatterns = [
     path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('news2', views.news2, name='news2'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('english', views.english, name='english'),
    path('english2', views.english2, name='english2'),
    path('english3', views.english3, name='english3'),
    path('english4', views.english4, name='english4'),
    path('english5', views.english5, name='english5')
]