from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from forum.models import Section, Subsection, Article, User, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class SectionList(generic.ListView):
    model = Section
    template_name = "forum/index.html"
    context_object_name = "sections"


class SubsectionDetail(generic.DeleteView):
    model = Subsection
    template_name = "forum/subsection.html"
    context_object_name = "subsection"


class ArticleDetail(generic.DeleteView):
    model = Article
    template_name = "forum/article.html"
    context_object_name = "article"


def add_comment(request, article_id, author_id):
    article = get_object_or_404(Article, pk=article_id)
    author = get_object_or_404(User, pk=author_id)
    comment = Comment()
    comment.article = article
    comment.author = author
    comment.text = request.POST["text"]
    comment.save()
    return HttpResponseRedirect(reverse('forum:article', args=(article.id,)))


def login_view(request):
    username = request.POST.get('username', "")
    password = request.POST.get('password', "")
    url_from = request.POST.get("url_from", "/")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Вы успешно вошли")
        return HttpResponseRedirect(url_from)
    else:
        messages.error(request, "Ошибка входа")
        return HttpResponseRedirect(url_from)


def logout_view(request):
    if request.method == "POST":
        url_from = request.POST.get("url_from", "/")
        logout(request)
        messages.success(request, "Вы вышли")
        return HttpResponseRedirect(url_from)
    elif request.method == "GET":
        logout(request)
        messages.success(request, "Вы вышли")
        return HttpResponseRedirect(reverse('forum:index'))


def register_view(request):
    username = request.POST.get("username")
    url_from = request.POST.get("url_from")
    password1 = request.POST.get("password")
    password2 = request.POST.get("password_repeat")
    if password1 == password2:
        user = User()
        user.username = username
        user.password = password1
        user.save()
        messages.success(request, "Аккаунт успешно создан")
    else:
        messages.error(request, "Пароли не совпадают")
    return HttpResponseRedirect(url_from)
