from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from forum.forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from forum.models import Section, Subsection, Article, User, Comment
from django.contrib import messages
from online_users.models import OnlineUserActivity


class SectionList(generic.ListView):
    model = Section
    template_name = "forum/index.html"
    context_object_name = "sections"

    def get_context_data(self, **kwargs):
        comments = Comment.objects.order_by("date")
        subsections_count = Subsection.objects.count()
        users_count = User.objects.count()
        new_user = User.objects.order_by('date_joined').last()
        context = super().get_context_data(**kwargs)
        users_online = self.get_online_users()
        context['online_users'] = users_online
        context['online_users_count'] = len(users_online)
        context['comments'] = comments
        context['subsections_count'] = subsections_count
        context['users_count'] = users_count
        context['new_user'] = new_user
        return context

    def get_online_users(self):
        user_activity_objects = OnlineUserActivity.get_user_activities()
        users_online = []
        for user_activity_object in user_activity_objects.all():
            users_online.append(get_object_or_404(User, pk=user_activity_object.pk))
        return users_online


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
    logout(request)
    messages.success(request, "Вы вышли")
    return HttpResponseRedirect(reverse('forum:index'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('forum:index')
    else:
        form = RegisterForm()
    return render(request, 'forum/register.html', {'form': form})


def profile(request, user_id):
    user_profile = get_object_or_404(User, pk=user_id)
    return render(request, "forum/profile.html", context={"user_profile": user_profile})
