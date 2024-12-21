from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def menu_view(request):
    return render(request, 'menu/menu.html')


def gift_view(request):
    return render(request, 'gift/gift.html')


def wishes_view(request):
    return render(request, 'wishes/index.html')


def contact_view(request):
    return render(request, 'contact/contact.html')
