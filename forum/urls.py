from django.urls import path
from forum.views import SectionList, ArticleDetail, SubsectionDetail

app_name = "forum"
urlpatterns = [
    path("", SectionList.as_view(), name="index"),
    path("article/<int:pk>", ArticleDetail.as_view(), name="article"),
    path("subsection/<int:pk>", SubsectionDetail.as_view(), name="subsection")
]
