from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Redirect to a success page
            login(request, user)
            return redirect('mainPage')
        else:
            # Return an invalid login
            messages.success(request, ("Возникла ошибка при попытке входа в аккаунт. Попробуйте снова!"))
            return redirect('signIn')
    else:
        context = {}
        return render(request, 'members/signIn.html', context)

def logout_user(request):
    username = request.user
    logout(request)
    messages.success(request, (f"Вы успешно вышли из аккаунта {username}"))
    return redirect('mainPage')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Регистрация успешна!"))
            return redirect('mainPage')
    else:
        form = RegisterUserForm()
    return render(request, 'members/signUp.html', {'form': form,})