from django.shortcuts import render
from django.http import HttpResponse
from forum.models import Article, Section, Subsection
from .models import MainPage, StartGamePage


def index(request):
    news = get_news()
    main_page = MainPage.objects.first()
    return render(request, "main/index.html", context={"news": news, "main_page": main_page})


def contacts(request):
    return HttpResponse("It's contacts page")


def start_game(request):
    start_game_page = StartGamePage.objects.first()
    return render(request, "main/start_game.html", {"start_game_page": start_game_page})


def get_news():
    section = Section.objects.filter(name="Основной раздел").first()
    subsection = Subsection.objects.filter(name="Новости").filter(section_id=section.id).first()
    news = Article.objects.filter(subsection_id=subsection.id).order_by('-date')
    return news


def page_not_found(request, exception):
    return render(request, "main/not_found.html")
