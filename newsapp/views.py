from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
import requests
import re
from bs4 import BeautifulSoup
import json
import string
from datetime import datetime, timedelta
# Create your views here.

@api_view(['GET'])
def UserInfo(request):
    userInfo = '''
    This API is created by ABIPRAVI '''
    author = '''
    Creator: Praveen Kumar
    About: This api collects news from websites and display as a api
    '''
    docs ='''
    Docs: Currently This api give only general news of india and Tech news 
    /news -> News [India]
    /tech -> Tech news
    
    [NOTE: Use JSON viewer extension to view api in good view]
    '''
    userInfo1 = {'Organixation': userInfo, "Author": author, "Docs": docs}

    return JsonResponse(userInfo1, safe=False)


@api_view(['GET'])
def getEnglishnews(request):
    news = []
    shotnews = []
    image = []
    link = []
    for i in range(0, 5):
        URL = "https://www.indiatoday.in/india/?page=" + str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="content")
        elements = results.find_all("div", class_="catagory-listing")
        for job_element in elements:
            title_element = job_element.find("h2")
            news.append(title_element.text.strip())
            image1 = job_element.find("img")
            image.append(image1['src'])
            location_element = ""
            if job_element.find("a", href=True):
                location_element = job_element.find("a", href=True)
                if location_element == "":
                    techlink.append("none")
                else:
                    link1 = 'https://www.indiatoday.in' + location_element['href']
                    link.append(link1)
            if job_element.find("p"):
                location_element = job_element.find("p")
                l1 = location_element.text.strip()
                location_element = l1
                shotnews.append(location_element)
    x = [{'news': a, 'image': s, 'link': t, 'shortnews': l} for a, s, t, l in zip(news, image, link, shotnews)]
    return JsonResponse(x, safe=False)

@api_view(['GET'])
def getTechnews(request):
    tech = []
    tech_image = []
    techlink = []

    for i in range(0, 5):
        print("page: ", i)
        URL = "https://www.indiatoday.in/technology/news?page=" + str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="content")
        elements = results.find_all("div", class_="catagory-listing")
        for job_element in elements:
            title_element = job_element.find("h2")
            image = job_element.find("img")
            tech_image.append(image['src'])
            tech.append(title_element.text.strip())
            if job_element.find("a", href=True):
                location_element = job_element.find("a", href=True)
                if location_element == "":
                    techlink.append("none")
                else:
                    link = 'https://www.indiatoday.in' + location_element['href']
                    techlink.append(link)
    x = [{'news': name, 'image': image, 'link': link} for name, image, link in zip(tech, tech_image, techlink)]
    return JsonResponse(x, safe=False)