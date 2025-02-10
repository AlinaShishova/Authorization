'''
Файл accounts/forms.py нужен для создания пользовательских форм с помощью Django Forms. Класс LoginForm наследуется от AuthenticationForm, стандартной формы Django для авторизации.
Поля username и password оформлены с кастомными CSS-классами для удобства.Django уже предоставляет стандартную форму аутентификации, но мы создаем свою, чтобы добавить стилизацию 
(например, для Bootstrap).
В Django формы используют виджеты (widget), чтобы определить, как поле формы будет отображаться в HTML. Виджет задает HTML-элемент (<input>, <textarea>, <select> и т. д.) и его атрибуты.
forms.TextInput - Это встроенный в Django виджет текстового поля, который рендерится в HTML как: <input type="text">. attrs — это словарь с HTML-атрибутами, который передается в виджет.
attrs={'class': 'form-control'} добавляет к <input> атрибут class="form-control", который применяется для стилизации.
'''


from django import forms  # Импортируем модуль forms для работы с формами в Django
from django.contrib.auth.forms import AuthenticationForm  # Импортируем стандартную форму аутентификации Django

# Создаем класс формы для входа в систему (авторизации)
class LoginForm(AuthenticationForm):
    # Поле для ввода имени пользователя (логина)
    username = forms.CharField(
        label="Имя пользователя",  # Отображаемый заголовок поля
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Виджет для текстового ввода с CSS-классом
    )

    # Поле для ввода пароля
    password = forms.CharField(
        label="Пароль",  # Отображаемый заголовок поля
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  # Виджет для ввода пароля (скрытый ввод)
    )
