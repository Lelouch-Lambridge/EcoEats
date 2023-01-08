from parse_ingredients import parse_ingredient
import re
from collections import OrderedDict
from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
from urllib.request import Request, urlopen
from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient
import nltk
import json
from googlesearch import search
import html2text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# stores url
url = 'https://tasty.co/recipe/pizza-dough'

# scrapes ingredients
scraper = scrape_me(
    url, wild_mode=True)

# removes unicode character
final_list_of_ingredients = scraper.ingredients()
for i in range(0, len(final_list_of_ingredients)):
    if '▢' in final_list_of_ingredients[i]:
        final_list_of_ingredients[i].replace('▢', '')

# list which contains each separate ingredient
listofinformation = []

# add all info to listofinformation
for i in range(0, len(final_list_of_ingredients)):
    listofinformation.append(parse_ingredient(final_list_of_ingredients[i]))
print(listofinformation)

ingredientednames = []
for j in range(0, len(listofinformation)):
    ingredientednames.append(listofinformation[j]['name'])

quantitiesforeach_ingredient = []
for k in range(0, len(listofinformation)):
    quantitiesforeach_ingredient.append(listofinformation[k]['quantity'])

unitforeach_ingredient = []
for i in range(0, len(listofinformation)):
    unitforeach_ingredient.append(listofinformation[i]['unit'])


# to search
googleTrendsUrl = 'https://google.com'
response = requests.get(googleTrendsUrl)
if response.status_code == 200:
    g_cookies = response.cookies.get_dict()

url = 'https://apps.carboncloud.com/climatehub/agricultural-reports/benchmarks/7859e28f-2971-4f86-836e-616f56eac8c2'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
x = soup.find_all('h2', class_='_c639719a')[0:2]

elementofcarbonnumber = []
for points in x:
    point = str(points.text)
    elementofcarbonnumber.append(point)

newcarbonvalues = []
newcarbonvalues.append(elementofcarbonnumber[0].replace('kg CO2e/kg', ''))
print(newcarbonvalues)
