from django.contrib import admin
from .models import MainPage, StartGamePage


class MainPageAdmin(admin.ModelAdmin):
    list_display = ['description']


class StartGamePageAdmin(admin.ModelAdmin):
    list_display = ['direct_link', 'torrent_link', 'google_drive_link']


admin.site.register(MainPage, MainPageAdmin)
admin.site.register(StartGamePage, StartGamePageAdmin)
