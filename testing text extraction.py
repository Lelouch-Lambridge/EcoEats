# test file
from urllib.request import urlopen
import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import OrderedDict
import re

url_test = input


def extractdata(url):
    r = requests.get(url)
    return r.text


listofparagraphs = []
listoflielements = []
listofspans = []

htmldata = extractdata(
    "https://sallysbakingaddiction.com/homemade-pizza-crust-recipe/")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all():
    listofparagraphs.append(data.get_text().replace('\n', '').strip())

print(listofparagraphs)

"""
for data in soup.find_all("span"):
    listofspans.append(data.get_text().replace('\n', '').strip())

datalist = soup.find('ul')
for li in datalist.find_all("li"):
    listoflielements.append(li.text.replace('\n', '').strip())

listofingredients = []

print(listofparagraphs)

for i in range(0, len(listofparagraphs)):
    if len(listofparagraphs[i]) == 0:
        print("")
    elif listofparagraphs[i][0].isdigit() or ord(listofparagraphs[i][0]) > 127:
        listofingredients.append(listofparagraphs[i])
print(listofingredients)

for i in range(0, len(listofspans)):
    if len(listofspans[i]) == 0:
        print("")
    elif listofspans[i][0].isdigit() or ord(listofspans[i][0]) > 127:
        listofingredients.append(listofspans[i])
print(listofingredients)

for i in range(0, len(listoflielements)):
    if len(listoflielements[i]) == 0:
        print("")
    elif listoflielements[i][0].isdigit() or ord(listoflielements[i][0]) > 127:
        listofingredients.append(listoflielements[i])
print(listofingredients)

print(listofingredients)
"""
