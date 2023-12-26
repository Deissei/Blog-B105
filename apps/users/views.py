from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model

from utils.generate_code import generate_code

User = get_user_model()


def logout_logics(request):
    logout(request)
    return redirect('login')


def login_logics(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:

            g = generate_code()
            print(g)
            user.is_person_code = g
            user.save()

            return redirect('is_person', user.id)
        
        error = "Неправильный логин или пароль!"
        return render(request, 'users/sign_in.html', locals())

    return render(request, 'users/sign_in.html')


def signup_logics(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        phone_number = request.POST['phone_number']

        if password != repassword:
            return render(request, 'users/sign_up.html', {'error': "Пароли не совподают!"})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'users/sign_up.html', {'error': "Такой пользователь уже есть!"})

        g = generate_code()
        print(g)
        user = User.objects.create_user(
            username=username,
            password=password,
            phone_number=phone_number,
            is_person_code=g,
        )

        return redirect('is_person', user.id)

    return render(request, 'users/sign_up.html')


def is_person(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)

        code = request.POST['code']

        if code == user.is_person_code:
            login(request, user)

            user.is_person_code = None
            user.save()

            return redirect('homepage')
        return render(request, 'users/is_person.html', {'error': "Неправильный код!"})

    return render(request, 'users/is_person.html')
