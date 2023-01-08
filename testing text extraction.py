from parse_ingredients import parse_ingredient
from bs4 import BeautifulSoup
import requests
from recipe_scrapers import scrape_me
from ingredient_parser import parse_ingredient
from googlesearch import search


def carbonfooter(url):
    # scrapes ingredients
    scraper = scrape_me(url, wild_mode=True)

    # removes unicode character
    final_list_of_ingredients = scraper.ingredients()
    for i in range(0, len(final_list_of_ingredients)):
        if '▢' in final_list_of_ingredients[i]:
            final_list_of_ingredients[i].replace('▢', '')

    # list which contains each separate ingredient
    print(listofinformation := [parse_ingredient(i)
          for i in (final_list_of_ingredients)])
    unitdict = {'cups': 0.25, 'teaspoons': 0.005,
                'tablespoons': 0.015, 'oz': 0.028, 'liters': 1, '': 1}
    carbon = 0
    for x in listofinformation:
        query = x['name'].split()[-1]
        print(query)
        if query in ['water', '']:
            continue
        url_list_foot = []
        try:
            from googlesearch import search
        except ImportError:
            print(" 'google' not found")
        query = 'carboncloud.com carbon footprint of ' + query
        for j in search(query, tld="com", num=1, stop=1, pause=2):
            if 'apps.carboncloud.com':
                url_list_foot.append(j)
            print(j)
        print(url_list_foot)
        url_foot = url_list_foot[0]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        y = soup.find_all('h2', class_='_c639719a')[0:2]
        elementofcarbonnumber = []
        for points in y:
            point = str(points.text)
            elementofcarbonnumber.append(point)
        try:
            foot = float(elementofcarbonnumber[0].replace('kg CO2e/kg', ''))
        except:
            foot = 0
        if x['unit'] in unitdict.keys():
            mod = unitdict[x['unit']]
        elif ''.join(x['unit'].split()[:-1]) in unitdict.keys():
            mod = unitdict[''.join(x['unit'].split()[:-1])]
        else:
            mod = 0

        carbon += float(x['quantity'])*mod*foot
        return carbon


print(carbonfooter('https://tasty.co/recipe/pizza-dough'))

# to search
#query= input('enter an ingredient name')
#url= "https://www.google.com/search?q=carbon+footprint+of " + query
