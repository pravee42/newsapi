from django.urls import path, include, re_path
# importing Views for routing
from . import views

urlpatterns = [
    path('', views.ArticlesClass.as_view())
]
