from django.shortcuts import render , redirect
from . import models
from .forms import Taskform
# Create your views here.
def index(request):
    tasks = models.Task.objects.all()
    form = Taskform()
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    context = {'tasks' : tasks , 'form' : form}
    return render(request ,'firstapp/index.html' , context=context)

def update(request , pk):
    task = models.Task.objects.get(id = pk)
    form = Taskform(instance=task)
    if request.method == 'POST':
        form = Taskform(request.POST , instance= task)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    context = {'form' : form}
    return render(request, 'firstapp/update_task.html',context= context)

def delete(request , pk):
    task = models.Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/home/')
    context = {'item' : task}
    return render(request , 'firstapp/delete_task.html',context=context)
