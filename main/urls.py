from django.urls import path
import main.views as views

app_name = 'main'
urlpatterns = [
   path('', views.index, name='index'),
   path('start_game', views.start_game, name='start_game')
]

handler404 = 'main.views.page_not_found'
