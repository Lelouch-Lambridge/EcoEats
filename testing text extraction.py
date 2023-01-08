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


# test file


"""
for i in range(0, len(listofparagraphs)):
    if len(listofparagraphs[i]) == 0:
        print("")
    elif listofparagraphs[i][0].isdigit() or ord(listofparagraphs[i][0]) > 127:
        listofingredients.append(listofparagraphs[i])

for i in range(0, len(listoflielements)):
    if len(listoflielements[i]) == 0:
        print("")
    elif listoflielements[i][0].isdigit() or ord(listoflielements[i][0]) > 127:
        listofingredients.append(listoflielements[i])

for i in range(0, len(listofingredients)):
    result = parse_ingredient(
        listofingredients[i])
    print(f"Found results: \n {result}")
"""

url = 'https://www.simplyrecipes.com/recipes/homemade_pizza/'
# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
scraper = scrape_me(
    url, wild_mode=True)


final_list_of_ingredients = scraper.ingredients()
for i in range(0, len(final_list_of_ingredients)):
    if '▢' in final_list_of_ingredients[i]:
        final_list_of_ingredients[i].replace('▢', '')

listofinformation = []

# add all info to listofinformation
for i in range(0, len(final_list_of_ingredients)):
    listofinformation.append(parse_ingredient(final_list_of_ingredients[i]))

ingredientednames = []
for j in range(0, len(listofinformation)):
    ingredientednames.append(listofinformation[j]['name'])


# to search
"""
for i in range(0, len(ingredientednames)):
    query = 'carbon cloud carbon footprint of ' + ingredientednames[i]
    number_of_carbon_links = 0
    not_carbonated = True
    while not_carbonated:
        for j in search(query, tld="com", num=number_of_carbon_links, stop=number_of_carbon_links, pause=2):
            if "apps.carboncloud.com" not in j:
                number_of_carbon_links += 1
                time.sleep(2)
            else:
                print(j)
                not_carbonated = False
"""
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
