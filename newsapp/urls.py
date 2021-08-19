from django.urls import path
from . import views
urlpatterns = [
    path('', views.UserInfo, name='Api DOCS'),
    path('news', views.getEnglishnews, name='getEnglishnews'),
    path('tech', views.getTechnews, name='getTechnews - Abipravi'),

]