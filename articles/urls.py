from django.urls import path, include, re_path
# importing Views for routing
from . import views

urlpatterns = [
    path('', views.ArticlesClass.as_view()),
    path('<int:pk>/', views.ArticlesDetail.as_view()),
    path('comments/', views.CommentsClass.as_view()),
    path('comments/<int:pk>/', views.CommentsDetail.as_view()),
]
