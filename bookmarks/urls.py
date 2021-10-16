from django.urls import path, include, re_path
from django.contrib import admin
# importing Views for routing
from . import views

urlpatterns = [
    path('', views.bookmark, name="book"),
    path('/get/<str:pk>', views.getBookmark, name="get"),
    path('/delete/<int:pk>', views.deletebookmark, name="delete")
]