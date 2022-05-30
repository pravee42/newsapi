from django.urls import path
from . import views
urlpatterns = [
    path('<str:pk>', views.getData, name="Get data")
]
