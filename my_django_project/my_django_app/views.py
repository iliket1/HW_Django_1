from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

# Create your views here.

def home_view(request):
    template_name = 'home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.datetime.now().time()
    return HttpResponse(f'Текущее время: {current_time}')

def workdir_view(request):
    path = os.getcwd()
    try:
        files = os.listdir(path)
        context = {
            'files': files
        }
        return render(request, 'workdir.html', context)
    except Exception as e:
        return HttpResponse(f'Ошибка: {str(e)}')