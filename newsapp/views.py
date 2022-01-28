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


@api_view(["GET"])
def UserInfo(request):
    userInfo = """
    This API is created by ABIPRAVI """
    author = """
    Creator: Praveen Kumar
    About: This api collects news from websites and display as a api
    """
    Routes = [
        {"Function": "news", "Route": "api/news"},
        {"Function": "tech news", "Route": "api/tech"},
        {"Function": "sports news", "Route": "api/sports"},
        {"Function": "latest sports news", "Route": "api/sports/latest"},
        {"Function": "business", "Route": "api/business"},
        {"Function": "economy news", "Route": "business/economy"},
        {"Function": "entrepreneurship", "Route": "api/entrepreneurship"},
        {"Function": "search", "Route": "api/search"},
        {"Function": "education", "Route": "api/education"},
        {"Function": "school", "Route": "api/education/school"},
        {"Function": "exam", "Route": "api/education/exam"},
        {"Function": "campus", "Route": "api/education/campus"},
    ]
    userInfo1 = {"Organixation": userInfo, "Author": author, "Docs": Routes}

    return JsonResponse(userInfo1, safe=False)


@api_view(["GET"])
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
            image.append(image1["src"])
            location_element = ""
            if job_element.find("a", href=True):
                location_element = job_element.find("a", href=True)
                if location_element == "":
                    techlink.append("none")
                else:
                    link1 = "https://www.indiatoday.in" + \
                        location_element["href"]
                    link.append(link1)
            if job_element.find("p"):
                location_element = job_element.find("p")
                l1 = location_element.text.strip()
                location_element = l1
                shotnews.append(location_element)
    x = [
        {"news": a, "image": s, "link": t, "shortnews": l}
        for a, s, t, l in zip(news, image, link, shotnews)
    ]
    return JsonResponse(x, safe=False)


@api_view(["GET"])
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
            tech_image.append(image["src"])
            tech.append(title_element.text.strip())
            if job_element.find("a", href=True):
                location_element = job_element.find("a", href=True)
                if location_element == "":
                    techlink.append("none")
                else:
                    link = "https://www.indiatoday.in" + \
                        location_element["href"]
                    techlink.append(link)
    x = [
        {"news": name, "image": image, "link": link}
        for name, image, link in zip(tech, tech_image, techlink)
    ]
    return JsonResponse(x, safe=False)


@api_view(["GET"])
def getSportsNews(request):
    URL = "https://news.google.com/search?q=sports&hl=en-IN&gl=IN&ceid=IN%3Aen"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="lBwEZb BL5WZb xP6mwf")
    elements = results.find_all(
        "div", class_="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc"
    )
    news = []
    link = []
    image = []
    for j in elements:
        news.append(j.find("h3").text)
        link1 = j.find("a")["href"]
        link1 = "https://news.google.com" + link1[1:]
        link.append(link1)
        image.append(j.find("img", class_="tvs3Id QwxBBf")["src"])
    x = [{"news": a, "image": s, "link": t}
         for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)


@api_view(["GET"])
def latestSportsnews(request):
    URL = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="lBwEZb BL5WZb GndZbb")
    elements = results.find_all(
        "div", class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
    news = []
    link = []
    image = []
    for j in elements:
        news.append(j.find("h3").text)
        link1 = j.find("a")["href"]
        link1 = "https://news.google.com" + link1[1:]
        link.append(link1)
        try:
            image.append(j.find("img", class_="tvs3Id QwxBBf")["src"])
        except:
            image.append(
                "https://th.bing.com/th/id/OIP.Bog_Pg2r3w4-dm6LBjQT-gHaFu?w=230&h=180&c=7&r=0&o=5&pid=1.7"
            )
    x = [{"news": a, "image": s, "link": t}
         for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)


@api_view(["GET"])
def seachquery(request, pk):
    URL = "https://news.google.com/search?q=" + pk + "&hl=en-IN&gl=IN&ceid=IN%3Aen"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="lBwEZb BL5WZb xP6mwf")
    elements = results.find_all(
        "div", class_="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc"
    )
    news = []
    link = []
    image = []
    for j in elements:
        news.append(j.find("h3").text)
        link1 = j.find("a")["href"]
        link1 = "https://news.google.com" + link1[1:]
        link.append(link1)
        try:
            image.append(j.find("img", class_="tvs3Id QwxBBf")["src"])
        except:
            image.append(
                "https://th.bing.com/th/id/OIP.Bog_Pg2r3w4-dm6LBjQT-gHaFu?w=230&h=180&c=7&r=0&o=5&pid=1.7"
            )

    x = [{"news": a, "image": s, "link": t}
         for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)
