# test file
import requests
import pandas as pd
from bs4 import BeautifulSoup

url_test = input


def extractdata(url):
    r = requests.get(url)
    return r.text


listofparagraphs = []
listoflielements = []

htmldata = extractdata(
    "https://www.allrecipes.com/recipe/10281/chewy-chocolate-cookies-ii/")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all("p"):
    listofparagraphs.append(data.get_text())

print("\n")
print("\n")

datalist = soup.find('ul')
for li in datalist.find_all("li"):
    listoflielements.append(li.text)

print(listoflielements)


stripped_list = [j.strip() for j in listoflielements]
stripped_listss = [j.replace('\n', '') for j in listoflielements]
for j in range(0, len(stripped_list)):
    stripped_list[j] == stripped_list[j].replace('\n', '')

print(stripped_list)
