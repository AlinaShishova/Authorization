## Чтобы запустить проект нужно:
1. ```
   pip install django psycopg2
   ```
   Команда используется для установки двух библиотек Python:

      a) Django — это популярный веб-фреймворк для создания веб-приложений на Python.

      b) psycopg2 — это библиотека для взаимодействия с базой данных PostgreSQL.
2. Настроить PostgreSQL, запомнить имя пользователя (обычно postgres) и пароль PostgreSQL. Я скачала pqAdmin4 для визуального отображения БД. Это необходимо для подключения приложения к БД в settings проекта.
   
    <img width="457" alt="image" src="https://github.com/user-attachments/assets/f164bffb-88b8-44a3-9ec8-165fea46fc48" />

   Рис.1 - settings.py в Project
3. Создать базу данных. У меня это "Project". Все остальные манипуляции с вводом пользователей (их логинов и паролей) производится через админку Django или Shell (см. пункт 9)
4. Выполнить миграции через команды:
   ```
   python manage.py makemigrations
   python manage.py
   ```
5. Создать суперпользователя (для доступа в админку):
   ```
   python manage.py createsuperuser
   ```
6. Следовать подсказкам: указать логин, пароль, подтвердить пароль.
7. Запустить сервер:
   ```
   python manage.py runserver
   ```
8. Перейти по адресу http://127.0.0.1:8000/accounts/login/ для проверки страницы авторизации
   
      <img width="227" alt="image" src="https://github.com/user-attachments/assets/8b56a90b-1b9a-436f-91f1-2dfc34413408" />

   Рис. 2 - Страничка авторизации

9. Чтобы создать записи о пользователях можно воспользоваться 2мя способами:

    а) Админкой Django:
       - Зайти по адреcу http://127.0.0.1:8000/admin/, авторизоваться через логин пароль суперпользователя

   <img width="940" alt="image" src="https://github.com/user-attachments/assets/d4f85c8b-6283-4291-a580-2bcd60e40f54" />
       - При нажатии на custom users +add можно добавить пользователя

   <img width="762" alt="image" src="https://github.com/user-attachments/assets/410a1e47-35d4-447e-b3c1-5620c57ba39f" />

   б) Через Shell:
       - Запустить shell
         ```
         python manage.py shell
         ```
    - далее команды:
         ```
         from accounts.models import User
         from django.contrib.auth.hashers import make_password

         user = CustomUser(login="user2", password=make_password("qwe123"))
         user.save()
         ```
 ___        
### Пояснение 

Структура каталогов и файлов

<img width="227" alt="image" src="https://github.com/user-attachments/assets/0a59e8cd-eac5-4d37-a737-0c9af518d4df" />

Корневая директория проекта (PROJECT/)
Это основная директория проекта Django, содержащая все файлы и папки, необходимые для работы веб-приложения.

<img width="225" alt="image" src="https://github.com/user-attachments/assets/7581af8a-3c13-4bd8-81db-1151b7746fe6" />

Project - основной проект. В нем важные файлы: 
   - settings.py - главный конфигурационный файл Django. Содержит настройки базы данных, установленные приложения, параметры аутентификации, статические файлы и другие          параметры.
   - urls.py - файл маршрутизации URL. Здесь определяются пути (routes), которые соответствуют определённым представлениям (views).
   - wsgi.py - используется для развертывания приложения на сервере (например, с Gunicorn или Apache). Запускает WSGI-приложение для обработки HTTP-запросов в production.

<img width="230" alt="image" src="https://github.com/user-attachments/assets/75ab70a6-70e7-419e-9bd4-59c34ec3a9a2" />

Директория accounts/ 

В этом каталоге содержатся файлы, относящиеся к приложению accounts, которое отвечает за аутентификацию и управление пользователями.
   - admin.py - Настраивает отображение модели пользователей в Django Admin.
   - models.py - Определяет модели базы данных
   - urls.py - Определяет маршруты для приложения accounts.
   - views.py - Описывает представления (логика обработки запросов).
   -  migrations/ - Хранит файлы миграций базы данных (изменения схемы БД).
   -  templates/ - Содержит HTML-шаблоны (например, login.html).




         

    
