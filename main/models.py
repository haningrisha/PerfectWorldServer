from django.db import models


class MainPage(models.Model):
    description = models.TextField()


class StartGamePage(models.Model):
    direct_link = models.CharField(max_length=360)
    torrent_link = models.CharField(max_length=360)
    google_drive_link = models.CharField(max_length=360)
