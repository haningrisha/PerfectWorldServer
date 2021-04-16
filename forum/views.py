from django.shortcuts import render
from forum.models import Section


def index(request):
    sections = Section.objects.all()
    return render(request, "forum/index.html", context={"sections": sections})
