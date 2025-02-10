# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    """
    Обрабатывает вход пользователя. При GET-запросе выводит форму,
    при POST — проверяет введённые данные.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Функция authenticate проверяет логин и пароль и возвращает объект пользователя, если данные корректны
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Сохраняем информацию о пользователе в сессии
            return redirect('home')  # Перенаправляем на главную страницу (предварительно создадим её)
        else:
            messages.error(request, 'Неверный логин или пароль')
    return render(request, 'login.html')