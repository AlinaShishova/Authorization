# accounts/admin.py

from django.contrib import admin  # Импортируем модуль для регистрации моделей в админке
from django.contrib.auth.admin import UserAdmin  # Импортируем стандартный класс админки для пользователей
from .models import CustomUser  # Импортируем нашу кастомную модель пользователя

# Создаём кастомную админку для управления пользователями
class CustomUserAdmin(UserAdmin):
    """
    Класс настройки отображения и управления пользователями в админ-панели Django.
    Наследуемся от UserAdmin, чтобы использовать стандартные функции администрирования.
    """

    model = CustomUser  # Указываем, что используем нашу кастомную модель пользователя

    # Поля, которые будут отображаться в списке пользователей в админке
    list_display = ('username', 'is_staff', 'is_active')

    # Поля, по которым можно фильтровать список пользователей
    list_filter = ('is_staff', 'is_active')

    # Группировка и отображение полей в форме редактирования пользователя
    fieldsets = (
        (None, {'fields': ('username', 'password')}),  # Основные поля
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),  # Раздел с правами доступа
    )

    # Поля, отображаемые при создании нового пользователя через админку
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # Дополнительный CSS-класс для улучшения отображения формы
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}  # Поля, доступные при добавлении нового пользователя
         ),
    )

    # Поля, по которым можно выполнять поиск пользователей в админке
    search_fields = ('username',)

    # Поля, по которым будет выполняться сортировка в списке пользователей
    ordering = ('username',)

# Регистрируем модель CustomUser в админке с указанными настройками
admin.site.register(CustomUser, CustomUserAdmin)
