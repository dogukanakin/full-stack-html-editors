from django.contrib import admin

from posts.models import Article, Page


admin.site.register(Article)
admin.site.register(Page)