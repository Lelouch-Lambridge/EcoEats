from parse_ingredients import parse_ingredient
from bs4 import BeautifulSoup
import pandas as pd
import requests
from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient
from googlesearch import search


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
# print(listofinformation)

ingredientednames = []
for j in range(0, len(listofinformation)):
    ingredientednames.append(listofinformation[j]['name'])

quantitiesforeach_ingredient = []
for k in range(0, len(listofinformation)):
    quantitiesforeach_ingredient.append(listofinformation[k]['quantity'])

unitforeach_ingredient = []
for i in range(0, len(listofinformation)):
    unitforeach_ingredient.append(listofinformation[i]['unit'])
print(listofinformation)

unitdict = {'cups': 0.25, 'teaspoons': 0.005,
            'tablespoons': 0.015, 'oz': 0.028, 'liters': 1, '': 1}
carbon = 0
for x in listofinformation:
    query = x['name']
    url_list = []
    try:
        from googlesearch import search
    except ImportError:
        print(" 'google' not found")
    query = 'carbon footprint' + query
    for j in search(query, tld="com", num=3, stop=3, pause=2):
        url_list.append(j)
    print(url_list)
    url = url_list[0]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    x = soup.find_all('h2', class_='_c639719a')[0:2]

    elementofcarbonnumber = []
    for points in x:
        point = str(points.text)
        elementofcarbonnumber.append(point)

    foot = float(elementofcarbonnumber[0].replace('kg CO2e/kg', ''))
    mod = unitdict[k] if (k := x['unit']) in unitdict.keys() else unitdict[j] if (
        j := ''.join(k.split()[:-1])) in unitdict.keys() else 0
    carbon += float(x['quantity'])*mod*foot

# to search
#query= input('enter an ingredient name')
    #url= "https://www.google.com/search?q=carbon+footprint+of " + query
