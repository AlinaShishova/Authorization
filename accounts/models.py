# accounts/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Менеджер для управления созданием пользователей и суперпользователей
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Создаёт и сохраняет обычного пользователя с указанным логином и паролем.
        :param username: Логин пользователя (обязательное поле)
        :param password: Пароль пользователя (по умолчанию None, но должен быть указан)
        :param extra_fields: Дополнительные поля пользователя (если есть)
        """
        if not username:
            raise ValueError('Логин должен быть указан')  # Проверяем, что передан логин
        
        # Создаём объект пользователя
        user = self.model(username=username, **extra_fields)
        # Устанавливаем (хэшируем) пароль
        user.set_password(password)
        # Сохраняем пользователя в базе данных
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Создаёт и сохраняет суперпользователя (администратора).
        :param username: Логин суперпользователя
        :param password: Пароль суперпользователя
        :param extra_fields: Дополнительные поля (is_staff, is_superuser)
        """
        extra_fields.setdefault('is_staff', True)  # Делаем суперпользователя сотрудником (доступ в админку)
        extra_fields.setdefault('is_superuser', True)  # Делаем суперпользователя суперюзером (полные права)

        # Проверяем, что переданные значения корректны
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True')

        return self.create_user(username, password, **extra_fields)

# Кастомная модель пользователя
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Кастомная модель пользователя, основанная на AbstractBaseUser.
    AbstractBaseUser предоставляет базовые поля для пользователя (например, password).
    PermissionsMixin добавляет поддержку прав и групп пользователей.
    """
    
    username = models.CharField(max_length=150, unique=True)  # Логин пользователя (уникальный)
    
    # Дополнительные поля
    is_active = models.BooleanField(default=True)  # Активен ли пользователь
    is_staff = models.BooleanField(default=False)  # Может ли пользователь заходить в админку

    # Указываем кастомный менеджер пользователей
    objects = CustomUserManager()

    # Поле, которое будет использоваться для аутентификации
    USERNAME_FIELD = 'username'

    # Поля, которые обязательно должны быть указаны при создании суперпользователя
    REQUIRED_FIELDS = []  # Можно добавить email или другие обязательные поля

    def __str__(self):
        """
        Возвращает строковое представление пользователя (его логин).
        """
        return self.username
