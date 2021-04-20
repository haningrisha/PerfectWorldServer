from django.urls import path
from forum.views import SectionList

app_name = "forum"
urlpatterns = [
    path("", SectionList.as_view(), name="index")
]
