from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main/index.html")


def contacts(request):
    return HttpResponse("It's contacts page")


def login(request):
    return render(request, "main/index.html", context={"login_message": "Успешно авторизирован"})


def register(request):
    return render(request, "main/index.html", context={"register_message": "Успешно зарегистрирован"})


def forget_password(request):
    return render(request, "main/index.html",
                  context={"forget_message": "Ссылка для востановления отправлена вам на почту"})
