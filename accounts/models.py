from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    login = models.CharField(max_length=50, unique=True)  # Логин (уникальный)
    password = models.CharField(max_length=255)  # Пароль (захеширован)

    def save(self, *args, **kwargs):
        """Перед сохранением хешируем пароль, если он не захеширован"""
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """Проверяем пароль"""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.login
