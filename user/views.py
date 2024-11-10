from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from user.forms import LoginForm, RegisterForm, UserUpdateForm, ProfileUpdateForm
from user.models import UserProfile


# Create your views here.
def user_logout(request):
    print(request.user)
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Oturum Açma Başarılı')
                return HttpResponseRedirect('/user/')
            else:
                messages.error(request, 'Oturum Açma Başarısız')
                return HttpResponseRedirect('/user/login')

    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username').lower()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # manuel profil oluşturma
                # current_user = user
                # userprofili = UserProfile()
                # userprofili.user = current_user
                # userprofili.save()
                messages.success(request, 'Kayıt Başarılı')
                return HttpResponseRedirect('/user/')
            else:
                messages.error(request, 'Kayıt Başarısız')
                return HttpResponseRedirect('/user/register')


    form = RegisterForm
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='/user/login/')
def user_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    context = {'profile': profile}
    return render(request, 'user_profile.html',context)

@login_required(login_url='/user/login/')
def user_update(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.userprofile)
    context = {'user_form': user_form, 'profile_form':profile_form}
    return render(request, 'user_update.html',context)