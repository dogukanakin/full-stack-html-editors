from unittest.mock import create_autospec
from venv import create
from django.urls import path, re_path

from . import views

from posts.views import home_page, create_page, list_pages, update_page, view_page


urlpatterns = [
    # home page
    path('', home_page, name='home_page'),

    # create page url
    path('page/create_page', create_page, name='create_page'),

    # list pages
    path('page/list_pages', list_pages, name='list_pages'),
    path('page/list_pages/<int:id>/', list_pages, name='list_pages'),
    path('page/update_page/<int:id>/', update_page, name='update_page'),
    path('page/view_page/<int:id>/', view_page, name='view_page'),
    path('api/pages', views.pages_list, name='pages_api'),
    path('api/pages/<int:id>', views.api_pages_view, name='pages_detail'),
    # article for that
    path('api/articles', views.articles_list, name='articles_api'),
    path('api/articles/<int:id>', views.api_articles_view, name='articles_detail'),

]
