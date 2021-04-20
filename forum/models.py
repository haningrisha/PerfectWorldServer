from django.db import models


class User(models.Model):
    nick = models.CharField(max_length=180)
    date_created = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.nick


class Section(models.Model):
    name = models.CharField(max_length=180)
    description = models.TextField()

    def __str__(self):
        return self.name


class Subsection(models.Model):
    name = models.CharField(max_length=180)
    description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Thread(models.Model):
    # analog of tag
    name = models.CharField(max_length=180)
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.name}, lvl {self.priority}"


class Article(models.Model):
    header = models.CharField(max_length=180)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True)
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE)

    def __str__(self):
        return self.header


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    response_to = models.OneToOneField('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
