from django.urls import path
from accounts.views import login_view, success_view, home  # Импортируем представления для страниц входа и успешного завершения

urlpatterns = [
    path('', home),
    # Маршрут для страницы авторизации
    # При переходе по адресу '/login/' будет вызвано представление login_view
    # name='login' позволяет ссылаться на этот маршрут по имени, например, через тег {% url 'login' %}
    path('login/', login_view, name='login'),

    # Маршрут для страницы успешного завершения (например, после успешного входа)
    # При переходе по адресу '/success/' будет вызвано представление success_view
    # name='success_page' позволяет ссылаться на этот маршрут по имени, например, через тег {% url 'success_page' %}
    path('success/', success_view, name='success'),
]
