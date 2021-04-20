from django.views import generic
from forum.models import Section, Subsection, Article


class SectionList(generic.ListView):
    model = Section
    template_name = "forum/index.html"
    context_object_name = "sections"


class SubsectionList(generic.DeleteView):
    model = Subsection
    template_name = "forum/subsection.html"
    context_object_name = "subsection"


class ArticleDetail(generic.DeleteView):
    model = Article
    template_name = "forum/article.html"
    context_object_name = "article"
