from django.forms import ModelForm
from django import forms
from . import models

class Taskform(ModelForm):

    class Meta:
        model = models.Task
        fields = ['title']
