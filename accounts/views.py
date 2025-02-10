from django.contrib.auth import login, authenticate  # Импортируем функции для аутентификации и авторизации пользователей
from django.shortcuts import render, redirect  # Импортируем функции для рендеринга шаблонов и перенаправлений
from .forms import LoginForm  # Импортируем форму для авторизации
from django.http import HttpResponse
from .models import User

from django.contrib.auth.hashers import check_password


def login_view(request):
    # Проверяем, был ли отправлен POST-запрос
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Создаём форму с данными, полученными из POST-запроса
        
        # Если форма валидна (поля заполнены корректно)
        if form.is_valid():
            username = form.cleaned_data['username']  # Получаем имя пользователя из формы
            password = form.cleaned_data['password']  # Получаем пароль из формы
            
            # Попытка аутентифицировать пользователя по имени и паролю
            try:
                user = User.objects.get(login=username)  # Проверяем, существует ли пользователь
                print(f"Найден пользователь: {user}")  # 🔍 Отладка
                if user.check_password(password):  # Проверяем пароль
                    print("Пароль верный! ✅")  # 🔍 Отладка
                    request.session['user_id'] = user.id  # Сохраняем пользователя в сессии
                    return redirect('success')  # Перенаправляем на защищённую страницу
                else:
                    print("Пароль неверный! ❌")  # 🔍 Отладка
                    form.add_error(None, 'Неверный пароль')
            except User.DoesNotExist:
                print("Пользователь не найден! ❌")  # 🔍 Отладка
                form.add_error(None, 'Пользователь не найден')
    else:
        form = LoginForm()  # Если запрос GET, то создаём пустую форму

    # Рендерим страницу с формой авторизации
    return render(request, 'login.html', {'form': form})  # Отправляем форму в шаблон для отображения



def success_view(request):
    return render(request, 'success.html')

def home(request):
    return HttpResponse('<h2>Главная</h2>')