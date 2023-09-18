from .models import Page  # Page modelinizi içe aktarın
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render

from posts.models import Article, Page
from posts.forms import ArticleForm, PageForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from posts.serializers import ArticleSerializer, PageSerializer
from django.http import JsonResponse
from django.core import serializers


def home_page(request):
    template_name = 'homepage.html'

    # query the articles and posts for the homepage
    articles = Article.objects.all()
    posts = Page.objects.all()
    context = {
        'articles': articles,
        'posts': posts
    }
    return render(request, template_name, context=context)


# Articles
def create_article(request):
    form = ArticleForm(request.POST or None)
    template_name = 'create_article'
    if request.method == 'POST':
        if form.is_valid():
            # save the form
            form.save()
            return redirect(home_page)

    context = {
        'form': form,
    }
    return render(request, template_name, context=context)


def update_article(request, id):
    get_article = Article.objects.get(id=id)
    form = ArticleForm(request.POST or None)
    template_name = 'update_article.html'
    context = {
        'article': get_article,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            # save the form
            form.save()
            return redirect(view_article, id)
    return render(request, template_name, context=context)


def view_article(request, id):
    get_article = Article.objects.get(id=id)
    template_name = 'view_article.html'

    context = {
        'article': get_article,
    }
    return render(request, template_name, context=context)


def delete_article(request, id):
    get_article = Article.objects.get(id=id)
    get_article.delete()
    return redirect(home_page)


# Pages
def create_page(request):
    form = PageForm(request.POST or None)
    template_name = 'create_page.html'
    if request.method == 'POST':
        if form.is_valid():
            # save the form
            form.save()
            return redirect(home_page)

    context = {
        'form': form,
    }
    return render(request, template_name, context=context)


def update_page(request, id):
    # get page
    get_page = Page.objects.get(id=id)

    # populate it with the instance
    form = PageForm(request.POST or None, instance=get_page)
    template_name = 'update_page.html'

    if request.method == 'POST':
        if form.is_valid():
            # save the form
            form.save()
            return redirect(view_page, id)

    context = {
        'page': get_page,
        'form': form,
    }
    return render(request, template_name, context=context)


def view_page(request, id):
    # get page
    get_page = Page.objects.get(id=id)
    template_name = 'view_page.html'

    # get the related pages
    related_pages = Page.objects.filter(
        article=get_page.article).exclude(id=id)

    context = {
        'page': get_page,
        'related_pages': related_pages,
    }
    return render(request, template_name, context=context)


def delete_page(request, id):
    # get page
    get_page = Page.objects.get(id=id)

    # delete the page
    get_page.delete()
    return redirect(home_page)


def list_pages(request, id):
    template_name = 'list_pages.html'
    # get the article
    get_article = Article.objects.get(id=id)
    pages = Page.objects.filter(article=get_article)
    context = {
        'pages': pages,
    }
    return render(request, template_name, context=context)


@api_view(['GET', 'POST', ])
def pages_list(request):
    if request.method == 'GET':
        data = Page.objects.all()

        serializer = PageSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_pages_view(request, id):
    try:
        page = Page.objects.get(id=id)
    except Page.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PageSerializer(page, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PageSerializer(
            page, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', ])
def articles_list(request):
    if request.method == 'GET':
        data = Article.objects.all()

        serializer = ArticleSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_articles_view(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(
            article, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
