import requests
from bs4 import BeautifulSoup

link = 'https://www.simplyrecipes.com/recipes/homemade_pizza/'

html = requests.get(link).text
soup = BeautifulSoup(html, "lxml")


with open('htmlfile.txt', 'a') as file:
    file.write(str(soup))
