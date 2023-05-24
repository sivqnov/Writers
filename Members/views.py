from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterProfileForm, RegisterUserForm
from .models import Profile
from django.contrib.auth.models import User
from Literature.models import Author, Genre, Work

# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.success(request, ("Возникла ошибка при попытке входа в аккаунт. Попробуйте снова!"))
                return redirect('login')
        else:
            context = {
                'title': 'Увайсці',
            }
            return render(request, 'login.html', context)

@login_required(login_url='login')
def logout_user(request):
    username = request.user
    logout(request)
    messages.success(request, (f"Вы успешно вышли из аккаунта {username}"))
    return redirect('main')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('user', user=str(request.user))
    else:
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            formProfile = RegisterProfileForm(request.POST)
            if form.is_valid() and formProfile.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                bio = formProfile.cleaned_data['bio']
                userobj = User.objects.get(username=username)
                Profile.objects.create(user=userobj, photo='default_user.png', bio=bio)
                messages.success(request, ("Рэгістрацыя паспяховая!"))
                return redirect('main')
        else:
            form = RegisterUserForm()
            formProfile = RegisterProfileForm()
        context = {
            'title': 'Рэгістрацыя',
            'form': form,
            'formProfile': formProfile,
            }
        return render(request, 'registration.html', context)

@login_required(login_url='login')
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    authors = Author.objects.filter()
    context = {
        'title': 'Профиль',
        'profile': profile,
    }
    return render(request, 'profile.html', context)