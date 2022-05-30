from django.shortcuts import render
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getData(request, pk):
    s = Service(ChromeDriverManager().install())
    url = 'https://twitter.com/' + pk
    photo_url = url + '/photo'
    bot = webdriver.Chrome(service=s)
    wait = WebDriverWait(bot, 20)
    bot.get(url)
    user_name = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/span[1]/span',
            )
        )
    ).text
    followers = ''
    try:
        followers = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span',
                )
            )
        ).text
    except:
        followers = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/a/span[1]/span',
                )
            )
        ).text
    following = ''
    try:
        following = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div[1]/a/span[1]/span',
                )
            )
        ).text
    except:
        following = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div[1]/a/span[1]/span',
                )
            )
        ).text
    tweets = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/div',
            )
        )
    ).text
    bot.get(photo_url)
    image = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/img',
            )
        )
    ).get_attribute("src")
    ss = tweets[:tweets.find(' T')]
    data = {'name': user_name, 'followers': followers,
            'following': following, 'profile': image, 'tweets': ss, 'follow': url}
    return Response(data)
