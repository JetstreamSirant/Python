from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

# Create your views here.

def index(request):
    return render(request, 'index.html')

def debug(request):
    # отладочная функция
    # её нужно будет удалить
    
    # используем её для работы с моделями
    obj_list = Advertisement.objects.all()
    print([o.title for o in obj_list])
    return HttpResponse("Успешно!")

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')