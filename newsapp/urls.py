from django.urls import path
from . import views
from . import education
from . import businessnews
from newsapp.trending import trending
urlpatterns = [
    path('', views.UserInfo, name='Api DOCS'),
    path('sports',views.getSportsNews, name="getSportsNews"),
    path('sports/latest',views.latestSportsnews, name="latestSportsnews"),
    path('news', views.getEnglishnews, name='getEnglishnews'),
    path('tech', views.getTechnews, name='getTechnews - Abipravi'),
    path('business', businessnews.business, name='business'),
    path('business/economy', businessnews.business_economy, name='businesseconomy'),
    path('business/market', businessnews.business_market, name='businessmarket'),
    path('business/entrepreneurship', businessnews.entrepreneurship, name='entrepreneurship'),
    path('search/<str:pk>', views.seachquery, name='seachquery'),
    path('education', education._news, name='news'),
    path('education/school', education.school_news, name='school'),
    path('education/exam', education.exam_news, name='seachquery'),
]
