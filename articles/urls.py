from django.urls import path, include, re_path
# importing Views for routing
from . import views

urlpatterns = [
    path('', views.post, name="post"),
    path('get/<str:pk>', views.get, name="get"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('update/<int:pk>', views.update, name="update")
]
