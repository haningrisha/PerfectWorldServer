from django.contrib import admin
from .models import Section, Subsection, Thread, Article, Comment, UserProfile


class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class SubsectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'description']


class ThreadAdmin(admin.ModelAdmin):
    list_display = ['name', 'priority']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['header', 'date', 'author', 'thread', 'subsection']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'date', 'author']


admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection, SubsectionAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)
