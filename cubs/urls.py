from django.urls import path
from .views import page1, page2,  page3, add_item, add_item2, add_item3, edit_item, edit_item2, edit_item3

urlpatterns = [
    path('page1/', page1, name='page1'),  # страница с кнопками
    path('page1/add/', add_item, name='add_item'),  # страница добавления формы
    path('page1/edit/', edit_item, name='edit_item'),  # страница добавления формы

    path('page2/', page2, name='page2'),
    path('page2/add/', add_item2, name='add_item2'),
    path('page2/edit/', edit_item2, name='edit_item2'),
    
    path('page3/', page3, name='page3'),
    path('page3/add/', add_item3, name='add_item3'),
    path('page3/edit/', edit_item3, name='edit_item3'),

    
]
