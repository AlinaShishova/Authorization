# accounts/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Менеджер для нашей модели пользователей
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Создаёт и сохраняет пользователя с заданным логином и паролем.
        """
        if not username:
            raise ValueError('Логин должен быть указан')
        # Создаём объект пользователя
        user = self.model(username=username, **extra_fields)
        # Хэшируем пароль с помощью встроенного метода
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Создаёт суперпользователя (админа) с заданными данными.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True')
            
        return self.create_user(username, password, **extra_fields)

# Собственно, модель пользователя
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    # Поле password уже определено в AbstractBaseUser (хранится в зашифрованном виде)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    # Поле для аутентификации – логин (username)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # можно добавить дополнительные обязательные поля, если потребуется

    def __str__(self):
        return self.username