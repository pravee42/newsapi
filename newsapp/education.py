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

@api_view(['GET'])
def exam_news(request):
    news = []
    link = []
    image = []
    for i in range(1,10):
        URL ="https://www.ndtv.com/education/exams-news?page=" + str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("div", class_="articles")
        elements = results.find_all("article")
        for j in elements:
            try:
                news.append(j.find("a").text)
                link1 = j.find("a")['href']
                link1 = "https://www.ndtv.com/" + link1[1:]
                link.append(link1)
            except:
                pass
            try:
                image.append(j.find("img", class_="lazy")["src"])
            except:
                image.append("https://th.bing.com/th/id/OIP.Bog_Pg2r3w4-dm6LBjQT-gHaFu?w=230&h=180&c=7&r=0&o=5&pid=1.7")

    x = [{'news': a, 'image': s, 'link': t} for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)

@api_view(['GET'])
def school_news(request):
    news = []
    link = []
    image = []
    for i in range(1,10):
        URL ="https://www.ndtv.com/education/school-news?page=" + str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("div", class_="articles")
        elements = results.find_all("article")
        for j in elements:
            try:
                news.append(j.find("a").text)
                link1 = j.find("a")['href']
                link1 = "https://www.ndtv.com/" + link1[1:]
                link.append(link1)
            except:
                pass
            try:
                image.append(j.find("img", class_="lazy")["src"])
            except:
                image.append("https://th.bing.com/th/id/OIP.Bog_Pg2r3w4-dm6LBjQT-gHaFu?w=230&h=180&c=7&r=0&o=5&pid=1.7")

    x = [{'news': a, 'image': s, 'link': t} for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)

@api_view(['GET'])
def _news(request):
    news = []
    link = []
    image = []
    for i in range(1,10):
        URL ="https://www.ndtv.com/education/latest-news?page=" + str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("div", class_="articles")
        elements = results.find_all("article")
        for j in elements:
            try:
                news.append(j.find("a").text)
                link1 = j.find("a")['href']
                link1 = "https://www.ndtv.com/" + link1[1:]
                link.append(link1)
            except:
                pass
            try:
                image.append(j.find("img", class_="lazy")["src"])
            except:
                image.append("https://th.bing.com/th/id/OIP.Bog_Pg2r3w4-dm6LBjQT-gHaFu?w=230&h=180&c=7&r=0&o=5&pid=1.7")

    x = [{'news': a, 'image': s, 'link': t} for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)