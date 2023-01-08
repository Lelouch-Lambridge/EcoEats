from recipe_scrapers import scrape_me
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


# give the url as a string, it can be url from any site listed below
scraper = scrape_me(
    'https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')

# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
scraper = scrape_me(
    'https://joyfoodsunshine.com/the-most-amazing-chocolate-chip-cookies/', wild_mode=True)

scraper.title()
scraper.total_time()
scraper.yields()
scraper.ingredients()
# or alternatively for results as a Python list: scraper.instructions_list()
scraper.instructions()
scraper.image()
scraper.host()
scraper.links()
print(scraper.ingredients())
