from django.shortcuts import render
from django.http import HttpResponse
from forum.models import Article, Section, Subsection


def index(request):
    news = get_news()
    return render(request, "main/index.html", context={"news": news})


def contacts(request):
    return HttpResponse("It's contacts page")


def start_game(request):
    return render(request, "main/start_game.html")


def get_news():
    section = Section.objects.filter(name="Основной раздел").first()
    subsection = Subsection.objects.filter(name="Новости").filter(section_id=section.id).first()
    news = Article.objects.filter(subsection_id=subsection.id).order_by('-date')
    return news
