from django.urls import path
from forum.views import SectionList, ArticleDetail, SubsectionDetail, add_comment, login_view, logout_view, register_view

app_name = "forum"
urlpatterns = [
    path("", SectionList.as_view(), name="index"),
    path("article/<int:pk>", ArticleDetail.as_view(), name="article"),
    path("subsection/<int:pk>", SubsectionDetail.as_view(), name="subsection"),
    path("article/<int:article_id>/comment/<int:author_id>", add_comment, name="comment"),
    path("article/<int:article_id>/comment/<int:author_id>/<int:response_to_id>", add_comment, name="response"),
    path("article/<int:article_id>/comment/<int:author_id>/<int:response_to_id>/<int:response_to_author_id>",
         add_comment, name="response_reply"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("register", register_view, name="register")
]
