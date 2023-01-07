# test file
import requests
import pandas as pd
from bs4 import BeautifulSoup

url_test = input


def extractdata(url):
    r = requests.get(url)
    return r.text


htmldata = extractdata("https://www.simplyrecipes.com/recipes/homemade_pizza/")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all("p"):
    print(data.get_text())

print("\n")
print("\n")

data1 = soup.find('ul')
for li in data1.find_all("li"):
    print(li.text, end=" ")
