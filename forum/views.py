from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from forum.models import Section, Subsection, Article, User, Comment
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


def add_comment(request, article_id, author_id, response_to_id=None, response_to_author_id=None):
    article = get_object_or_404(Article, pk=article_id)
    author = get_object_or_404(User, pk=author_id)
    comment = Comment()
    comment.article = article
    comment.author = author
    comment.text = request.POST["text"]
    if response_to_id is not None:
        response_to = get_object_or_404(Comment, pk=response_to_id)
        comment.response_to = response_to
    if response_to_author_id is not None:
        response_to_author = get_object_or_404(User, pk=response_to_author_id)
        comment.response_to_author = response_to_author
    comment.save()
    messages.success(request, f"Комментарий \"{comment}\" добавлен")
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


def profile(request, user_id):
    user_profile = get_object_or_404(User, pk=user_id)
    return render(request, "forum/profile.html", context={"user_profile": user_profile})
