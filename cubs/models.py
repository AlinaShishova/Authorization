from django.db import models
from django.conf import settings  # Берём кастомного пользователя
from accounts.models import CustomUser  # Импорт вашей модели пользователя

class Page(models.Model):
    """Модель страницы"""
    name = models.CharField(max_length=255, verbose_name="Название страницы")
    slug = models.SlugField(unique=True, verbose_name="Уникальный идентификатор")

    def __str__(self):
        return self.name

class PageManager(models.Model):
    """Модель для хранения менеджеров страниц"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Менеджер")
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name="Страница")

    class Meta:
        unique_together = ('user', 'page')  # Один пользователь не может быть менеджером одной страницы дважды

    def __str__(self):
        return f"{self.user.username} - Менеджер {self.page.name}"
