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
def business(request):
    URL ="https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="lBwEZb BL5WZb GndZbb")
    elements = results.find_all("div", class_="DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf")
    news = []
    link = []
    image = []
    for j in elements:
        news.append(j.find("h3").text)
        link1 = j.find("a")['href']
        link1 = "https://news.google.com" + link1[1:]
        link.append(link1)
        try:
            image.append(j.find("img", class_="tvs3Id QwxBBf")["src"])
        except:
            image.append("https://th.bing.com/th/id/OIP.Bog_Pg2r3w4-dm6LBjQT-gHaFu?w=230&h=180&c=7&r=0&o=5&pid=1.7")
        x = [{'news': a, 'image': s, 'link': t} for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)

@api_view(['GET'])
def business_economy(request):
    URL ="https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ/sections/CAQiTENCQVNNd29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1HZG1jSE16S2dzU0NTOXRMekJuWm5Cek15Z0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURsek1XWVNCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="lBwEZb BL5WZb GndZbb")
    elements = results.find_all("div", class_="DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf")
    news = []
    link = []
    image = []
    for j in elements:
        news.append(j.find("h3").text)
        link1 = j.find("a")['href']
        link1 = "https://news.google.com" + link1[1:]
        link.append(link1)
        try:
            image.append(j.find("img", class_="tvs3Id QwxBBf")["src"])
        except:
            image.append("https://th.bing.com/th/id/OIP.Bog_Pg2r3w4-dm6LBjQT-gHaFu?w=230&h=180&c=7&r=0&o=5&pid=1.7")
    x = [{'news': a, 'image': s, 'link': t} for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)

@api_view(['GET'])
def business_market(request):
    URL ="https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ/sections/CAQiYENCQVNRZ29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1EbDVOSEJ0S2hvS0dBb1VUVUZTUzBWVVUxOVRSVU5VU1U5T1gwNUJUVVVnQVNnQSouCAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="lBwEZb BL5WZb GndZbb")
    elements = results.find_all("div", class_="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc")
    news = []
    link = []
    image = []
    for j in elements:
        news.append(j.find("h3").text)
        link1 = j.find("a")['href']
        link1 = "https://news.google.com" + link1[1:]
        link.append(link1)
        try:
            image.append(j.find("img", class_="tvs3Id QwxBBf")["src"])
        except:
            image.append("https://th.bing.com/th/id/OIP.Bog_Pg2r3w4-dm6LBjQT-gHaFu?w=230&h=180&c=7&r=0&o=5&pid=1.7")
    x = [{'news': a, 'image': s, 'link': t} for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)

@api_view(['GET'])
def entrepreneurship(request):
    URL ="https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ/sections/CAQiSkNCQVNNUW9JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ESnVkM0VxQ2hJSUwyMHZNREp1ZDNFb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="lBwEZb BL5WZb GndZbb")
    elements = results.find_all("div", class_="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc")
    news = []
    link = []
    image = []
    for j in elements:
        news.append(j.find("h3").text)
        link1 = j.find("a")['href']
        link1 = "https://news.google.com" + link1[1:]
        link.append(link1)
        try:
            image.append(j.find("img", class_="tvs3Id QwxBBf")["src"])
        except:
            image.append("https://th.bing.com/th/id/OIP.Bog_Pg2r3w4-dm6LBjQT-gHaFu?w=230&h=180&c=7&r=0&o=5&pid=1.7")

    x = [{'news': a, 'image': s, 'link': t} for a, s, t in zip(news, image, link)]
    return JsonResponse(x, safe=False)