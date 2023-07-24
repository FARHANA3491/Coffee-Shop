from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('prod/',views.index,name='index'),
    # path('book/',views.booking,name='booking'),
    path('booknow/',views.booknow,name='booknow'),
   
]
