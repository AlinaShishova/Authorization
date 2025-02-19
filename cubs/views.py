from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied
from functools import wraps
from cubs.models import Page, PageManager



"""Декоратор для проверки, является ли пользователь менеджером страницы."""
def manager_required(page_slug):
    def decorator (view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
        
            # Проверяем, является ли пользователь менеджером
            if not PageManager.objects.filter(user=request.user, page__slug=page_slug).exists():
                raise PermissionDenied("Доступ запрещен")

            return view_func(request, *args, **kwargs)

        return _wrapped_view
    return decorator


"""Страницы с кнопками управления"""

# Первая страница
@manager_required("page1")
def page1(request):
    return render(request, "page1.html")


# Вторая страница
@manager_required("page2")
def page2(request):
    return render(request, "page2.html")


# Третья страница
@manager_required("page3")
def page3(request):
    return render(request, "page3.html")




"""Декоратор, который проверяет, состоит ли пользователь в группе с именем group_name."""

def group_required(group_name):
    def in_group(user):
        return user.groups.filter(name=group_name).exists()
    return user_passes_test(in_group)


# Страницы добавления

@login_required
@group_required('Создатели')  # Только пользователи, принадлежащие группе "Создатели", могут создавать объекты
def add_item(request):
    # Логика создания объекта
    return render(request, 'add.html')

@login_required
@group_required('Создатели')  # Только пользователи, принадлежащие группе "Создатели", могут создавать объекты
def add_item2(request):
    # Логика создания объекта
    return render(request, 'add2.html')

@login_required
@group_required('Создатели')  # Только пользователи, принадлежащие группе "Создатели", могут создавать объекты
def add_item3(request):
    # Логика создания объекта
    return render(request, 'add3.html')

# Страницы редактирования
  
@login_required
@group_required('Редакторы')  # Только "Редакторы" могут редактировать
def edit_item(request):
    # Логика редактирования объекта
    return render(request, 'edit.html')

@login_required
@group_required('Редакторы')  # Только "Редакторы" могут редактировать
def edit_item2(request):
    # Логика редактирования объекта
    return render(request, 'edit2.html')

@login_required
@group_required('Редакторы')  # Только "Редакторы" могут редактировать
def edit_item3(request):
    # Логика редактирования объекта
    return render(request, 'edit3.html')

# @login_required
# @group_required('Удаляющие')  # Только пользователи из группы "Удаляющие" могут удалять
# def delete_page(request):
#     # Логика удаления объекта
#     return 