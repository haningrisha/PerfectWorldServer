from django.urls import path
import main.views as views

app_name = 'main'
urlpatterns = [
   path('', views.index, name='index'),
   path('login', views.login, name='login'),
   path('register', views.register, name='register'),
   path('forget_password', views.forget_password, name='forget_password')
]
