from django.urls import path
from .views import *
app_name = 'todoapp'

urlpatterns = [
    path('home/' , index ,name = 'home'),
    path('update/<int:pk>/',update ,name = 'update'),
    path('delete/<int:pk>/', delete, name='delete'),
]