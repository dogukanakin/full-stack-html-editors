from django.forms import ModelForm
from django import forms
from posts.models import Article, Page

# Import Froala Editor Widget from froala_editor.widget
from froala_editor.widgets import FroalaEditor


class PageForm(ModelForm):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'class': 'w-full focus:ring-0 h-full focus:outline-none text-2xl'}))

    # Enable the froala widget for the custom model form
    content = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Page
        fields = '__all__'


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
