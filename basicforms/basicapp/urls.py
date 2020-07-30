from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index,name='index'),
    path('form',views.form_name_view,name = 'YOYO')
]