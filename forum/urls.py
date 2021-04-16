from django.urls import path
from forum.views import index

urlpatterns = [
    path("", index)
]
