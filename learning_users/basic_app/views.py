from django.shortcuts import render
from .forms import UserProfileInfoForm , UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    my_dic = {'insert_me': "Hello it worked"}
    return render(request,'basic_app/index.html',context=my_dic)

def special(request):
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    user_form = UserForm()
    profile_form = UserProfileInfoForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    dd = {'registered':registered,'user_form':user_form,
          'profile_form':profile_form}
    return render(request,'basic_app/registration.html',context=dd)




def user_login(request):

    if request.method=='POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username , password= password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print('Someone Tried to login')
            return HttpResponse('Invalif Login Details !!')

    else:
        return render(request,'basic_app/login.html',{})
