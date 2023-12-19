from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def logout_logics(request):
    logout(request)
    return redirect('login')


def login_logics(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        
        error = "Неправильный логин или пароль!"
        return render(request, 'users/sign_in.html', locals())

    return render(request, 'users/sign_in.html')


def signup_logics(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password != repassword:
            return render(request, 'users/sign_up.html', {'error': "Пароли не совподают!"})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'users/sign_up.html', {'error': "Такой пользователь уже есть!"})
        
        user = User.objects.create_user(
            username=username,
            password=password,
        )
        login(request, user)
        return redirect('homepage')

    return render(request, 'users/sign_up.html')
