from django.urls import path
from . import views
from newsapp.trending import trending
urlpatterns = [
    path('', views.UserInfo, name='Api DOCS'),
    path('sports',views.getSportsNews, name="getSportsNews"),
    path('latestsports',views.latestSportsnews, name="latestSportsnews"),
    path('news', views.getEnglishnews, name='getEnglishnews'),
    path('tech', views.getTechnews, name='getTechnews - Abipravi'),
    #path('trending', trending, name='trending'),
]
