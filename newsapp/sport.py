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