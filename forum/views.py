from django.shortcuts import render, get_list_or_404
from forum.models import Section


def index(request):
    sections = get_list_or_404(Section.objects.all())
    return render(request, "forum/index.html", context={"sections": sections})
