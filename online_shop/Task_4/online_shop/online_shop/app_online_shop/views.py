from django.shortcuts import render
# подключаем объект для выполнения http-запросов
from django.http import HttpResponse
from .models import advertisements

# Create your views here.

def index(request):
    online_shops = advertisements.objects.all()
    # Создаем контекст шаблона
    context = {
        'online_shops': online_shops
        }
    return render(request, 'index.html', context)
def top_sellers(request):
    return render(request, 'top_sellers.html')
def advertisement_post(request):
    return render(request, 'advertisement_post.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
def profile(request):
    return render(request, 'profile.html')
def advertisement(request):
    return render(request, 'advertisement.html')