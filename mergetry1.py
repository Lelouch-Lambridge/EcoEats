from recipe_scrapers import scrape_html
import requests
from recipe_scrapers import scrape_me

try:
    from googlesearch import search
except ImportError:
    print(" 'google' not found")

while True:
    prompt = input('Enter your search prompt: ').split( )
    if len(prompt) > 5:
        print('Enter a shorter search')
    else:
        break
prompt = str(prompt)
query = prompt + ' recipe'

url_list = []

while len(url_list) <= 3:
    for j in search(query, tld="com", num=20, stop=20, pause=0):
        if 'allrecipe' in j:
            url_list.append(j)
            if len(url_list) >= 3:
                break
url_list.pop()
for i in url_list:
    scraper = scrape_me(
    i[0], wild_mode=True)

scraper.title()
scraper.total_time()
scraper.yields()
scraper.ingredients()
# or alternatively for results as a Python list: scraper.instructions_list()
scraper.instructions()
scraper.image()
scraper.host()
scraper.links()
print(scraper.nutrients())
