from django.urls import path
from .views import page1

urlpatterns = [
    path('', page1, name='page1'),  # страница с кнопками
    
]
