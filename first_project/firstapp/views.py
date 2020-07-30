from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dic = {'insert_me' : "Hello it worked"}
    return render(request , 'firstapp/index.html',context=my_dic)

def fun2(request):
    return HttpResponse('2Nd Page')