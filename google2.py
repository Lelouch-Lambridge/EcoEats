import requests
from bs4 import BeautifulSoup
query=input()
"""
url = 'https://www.google.com'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))"""

"""from bs4 import BeautifulSoup
import requests

search = 'your search terms here.'
url = 'https://www.google.com/search'

headers = {
	'Accept' : '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}
parameters = {'q': search}

content = requests.get(url, headers = headers, params = parameters).text
soup = BeautifulSoup(content, 'html.parser')

search = soup.find(id = 'search')
first_link = search.find('a')

print(first_link['href'])"""
url = 'https://www.google.ru/search?q=' + str(query)
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
links = soup.findAll('cite')
print([link.text for link in links])
