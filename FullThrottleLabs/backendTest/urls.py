from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index),
    path('addActivityPeroid', views.addActivityPeroid),
    path('addUser', views.addUser),
    path('api', views.api)
]
