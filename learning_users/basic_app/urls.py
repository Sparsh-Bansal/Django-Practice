from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('home/',views.index,name='index'),
    path('login/',views.user_login,name='Login'),
]