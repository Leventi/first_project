from django.http import HttpResponse
from django.shortcuts import render, reverse

import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.today().strftime("%H:%M - %Y/%m/%d")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/workdir.html'
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории

    tree = []

    for dirname, dirnames, filenames in os.walk('.'):
        for subdirname in dirnames:
            tree.append(os.path.join(dirname, subdirname))

        for filename in filenames:
            tree.append(os.path.join(dirname, filename))

        if 'venv' in dirnames:
            dirnames.remove('venv')

        if '.idea' in dirnames:
            dirnames.remove('.idea')

    context = {
        'title': 'Дерево каталога',
        'tree': tree
    }

    return render(request, template_name, context)
