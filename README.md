## Чтобы запустить проект нужно:
1. ```
   pip install django psycopg2
   ```
   Команда используется для установки двух библиотек Python:

      a) Django — это популярный веб-фреймворк для создания веб-приложений на Python.

      b) psycopg2 — это библиотека для взаимодействия с базой данных PostgreSQL.
3. Настроить PostgreSQL, запомнить имя пользователя (обычно postgres) и пароль PostgreSQL. Я скачала pqAdmin4 для визуального отображения БД. Это необходимо для подключения приложения к БД в settings проекта.
   
    <img width="457" alt="image" src="https://github.com/user-attachments/assets/f164bffb-88b8-44a3-9ec8-165fea46fc48" />

   Рис.1 - settings.py в Project
5. Создать базу данных. У меня это "Project". Все остальные манипуляции с вводом пользователей (их логинов и паролей) производится через админку Django или Shell (см. пункт 10)
6. Выполнить миграции через команды:
   ```
   python manage.py makemigrations
   python manage.py
   ```
7. Создать суперпользователя (для доступа в админку):
   ```
   python manage.py createsuperuser
   ```
8. Следовать подсказкам: указать логин, пароль, подтвердить пароль.
9. Запустить сервер:
   ```
   python manage.py runserver
   ```
10. Перейти по адресу http://127.0.0.1:8000/accounts/login/ для проверки страницы авторизации
   
      <img width="227" alt="image" src="https://github.com/user-attachments/assets/8b56a90b-1b9a-436f-91f1-2dfc34413408" />

   Рис. 2 - Страничка авторизации

11. Чтобы создать записи о пользователях можно воспользоваться 2мя способами:

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
         


         

    
