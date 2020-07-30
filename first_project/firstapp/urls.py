from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from firstapp import views

urlpatterns = [
    path('1/',views.index,name='index'),
    path('2/',views.fun2,name='fun2')
]