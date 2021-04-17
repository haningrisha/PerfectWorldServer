from django.urls import path
from forum.views import index

app_name = "forum"
urlpatterns = [
    path("", index, name="index")
]
