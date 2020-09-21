from django.shortcuts import render
from myapp.forms import UserForm ,UserProfileInfoForm
from . import views ,urls
from django.conf.urls import url

from django.contrib.auth import login ,logout , authenticate
from django.urls import get_resolver ,reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse ,HttpResponseRedirect


def index(request):
    dict = {'insert_me':"im inserted from index"}
    return render(request,'myapp/index.html', context=dict)
# Create your views here.
@login_required
def special(request):
    return HttpResponse("you are logged in ! ,")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def reg(request):
    registered =False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'pics' in request.FILES:
                profile.profile_pic = request.FILES['pics']
            profile.save()
            registered =True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form =UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'myapp/reg.html',{
                'user_form':user_form,
                'profile_form':profile_form,
                'registered':registered,


    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password= password)

        if user :
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Acaount is not active!")
        else:
            print("some want to login but faild !")
            return HttpResponse("invild login")
    else:
        return render(request,"myapp/login.html",{})
