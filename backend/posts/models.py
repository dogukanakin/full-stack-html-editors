from django.db import models
from froala_editor.fields import FroalaField
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    articleTitle = models.CharField(max_length=255)

    def __str__(self):
        return self.articleTitle


class Page(models.Model):
    pageTitle = models.CharField(max_length=255)
    # Froala WYSIWYG Editor
    contentFrola = FroalaField()
    contentCkEditor = RichTextUploadingField()

    # Relate the page to an article by using ForeignKey
    articleTitleforPage = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pageTitle} part of {self.articleTitleforPage.articleTitle}'
