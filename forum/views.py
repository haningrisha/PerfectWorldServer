from django.views import generic
from django.shortcuts import redirect, get_object_or_404
from forum.models import Section, Subsection, Article, User


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
    
