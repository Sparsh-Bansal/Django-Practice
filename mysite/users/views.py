from django.shortcuts import render , redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm , UserProfileForm
# Create your views here.

def register(request):
    form = forms.UserRegisterForm()

    if request.method=='POST':
        form = forms.UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created Successfully')
            return redirect('login')

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = UserProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)


    contextt = {
        'u_form' : u_form ,
        'p_form' : p_form
    }

    return render(request,'users/profile.html',context=contextt)


