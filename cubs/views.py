from django.shortcuts import render

def page1(request):
    """страница с кнопками управления"""
    return render(request, 'page1.html')