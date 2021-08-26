import requests
import re
from bs4 import BeautifulSoup
import json
import string
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from datetime import datetime, timedelta


URL = "https://www.indiatoday.in/trending-news"
img = []
news = []
link = []
shortnews = []
x = {}

@api_view(['GET'])
def trending(request):
    for i in range(0, 3):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="view-content")
        elements = results.find_all("div", class_="catagory-listing")
        for j in elements:
            image = j.find("img")
            headlines = j.find("h2")
            isduplicate = duplicate_news(headlines.text.strip())
            if isduplicate != 1:
                img.append(image["src"])
                news.append(headlines.text.strip())
                p = j.find("p")
                shortnews.append(p.text.strip())
                link1 = j.find("a")
                link.append(link1["href"])
    news1 = news[0:13]
    x = [{'news': a, 'image': s, 'link': t, 'shortnews': l} for a, s, t, l in zip(news1, img, link, shortnews)]
    return JsonResponse(x, safe=False)

