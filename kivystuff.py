from ingredient_parser import parse_ingredient
from recipe_scrapers import scrape_me
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.app import App
import kivy
kivy.require("2.1.0")
#from kivy.uix.label import Label
#from kivy.uix.button import Button
#from kivy.uix.textinput import TextInput
#from kivy.uix.gridlayout import GridLayout


Builder.load_file('kivystuff.kv')


def carbonfooter(url):
    # scrapes ingredients
    scraper = scrape_me(url, wild_mode=True)

    # removes unicode character
    final_list_of_ingredients = scraper.ingredients()
    for i in range(0, len(final_list_of_ingredients)):
        if '▢' in final_list_of_ingredients[i]:
            final_list_of_ingredients[i].replace('▢', '')

    # list which contains each separate ingredient
    listofinformation = [parse_ingredient(i) for i in (final_list_of_ingredients)]
    unitdict = {'cups': 0.25, 'teaspoons': 0.005, 'tablespoons': 0.015, 'oz': 0.028, 'liters': 1, '': 1}
    carbon = 0

    for x in listofinformation:
        query = x['name'].split()[-1]
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
        mod = unitdict[k] if (k := x['unit']) in unitdict.keys() else unitdict[j] if (j := ''.join(k.split()[:-1])) in unitdict.keys() else 0
        print(float(x['unit']), mod, foot)
        carbon += float(x['quantity'])*mod*foot
        print(carbon)
        return carbon if type(carbon) == float else 0.0

# where google search function would go


def find(stuff):
    # return ' '.join(stuff.split()[2:]), '0'

    try:
        from googlesearch import search
    except ImportError:
        print(" 'google' not found")
    prompt = str(' '.join(stuff.split()[2:]))
    query = prompt + ' recipe'

    url_list = []
    e = 0 
    while len(url_list) < 4:
        for j in search(query, tld="com", num=5, start = e, stop= e+5, pause=0):
            if not ('youtube' in j or 'tiktok' in j or 'pintrest' in j or 'facebook' in j or '.gov' in j or 'delish' in j or 'foodnetwork' in j):
                url_list.append(j)
    url_list.pop()
    print(url_list)
    return url_list


def see(stuff):
    out = []
    for n in (k := find(stuff)):
        out += [(k, carbonfooter(n))]


class MyLayout(Widget):
    def press(self):
        words = self.ids.txt_in.text
        print(tuplist := see(words))
        
        while len(tuplist) > 5: tuplist.pop()
        print(tuplist)
        for n in range(len(tuplist)): exec(f"self.ids.re{n}.text, self.ids.c{n}.text = tuplist[{n}]")
        self.ids.txt_in.text = 'Enter word: '
        return words


class MyApp(App):
    def build(self): return MyLayout()


MyApp().run()
