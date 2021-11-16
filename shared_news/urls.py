from django.urls import path, include, re_path
from django.contrib import admin
# importing Views for routing
from . import views

urlpatterns = [
    path('post', views.add_news_to_db, name="news"),
    path('<str:pk>',
         views.getsharedNews, name="get_news")
]
