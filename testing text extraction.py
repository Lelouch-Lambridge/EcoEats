from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient
import nltk

nltk.download('averaged_perceptron_tagger')
"""
# test file
from urllib.request import urlopen
import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
from parse_ingredients import parse_ingredient


url_test = input


def extractdata(url):
    r = requests.get(url)
    return r.text


listofparagraphs = []
listoflielements = []
listofspans = []
listofingredients = []

htmldata = extractdata(
    "https://www.theseasonedmom.com/easiest-burrito-recipe/")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all():
    listofparagraphs.append(data.get_text().replace('\n', '').strip())

"""
"""
from recipe_scrapers import scrape_me
datalist = soup.find('ul')
for li in datalist.find_all("li"):
    listoflielements.append(li.text.replace('\n', '').strip())
"""
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


# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
scraper = scrape_me(
    'https://www.simplyrecipes.com/recipes/homemade_pizza/', wild_mode=True)

# list of ingredients obtained from scraping
final_list_of_ingredients = scraper.ingredients()
for i in range(0, len(final_list_of_ingredients)):
    if '▢' in final_list_of_ingredients[i]:
        final_list_of_ingredients[i].replace('▢', '')

listofinformation = []

# add all info to listofinformation
for i in range(0, len(final_list_of_ingredients)):
    listofinformation.append(parse_ingredient(final_list_of_ingredients[i]))

for j in range(0, len(listofinformation)):
    print(listofinformation[j])
    print('\n')
