"""import requests
from bs4 import BeautifulSoup
query=input()"""
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
"""url = 'https://www.google.ru/search?q=' + str(query)
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
links = soup.findAll('cite')
print([link.text for link in links])"""
"""from bs4 import BeautifulSoup
import requests

urls=[]"""

"""def scrape(site):
    r=requests.get(site)
    s=BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("a"):
        href= i.attrs['href']
        if href.startswith("/"):
            site=site+href
            if site not in urls:
                urls.append(site)
                print(site)
                scrape(site)
if __name__ =="__main__":
    site= 'https://www.google.com/search?q=cheese'
    scrape(site)"""
"""from urllib.parse import urlencode, urlparse, parse_qs

from lxml.html import fromstring
from requests import get

raw = get("https://www.google.com/search?q=StackOverflow").text
page = fromstring(raw)

for result in page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
    print(url[0])"""
class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='com',lang='en',num=10,stop=3,pause=2):
         count += 1
         print(i + '\n')
if __name__=='__main__':
   gs = Gsearch_python("vegan cookies")
   gs.Gsearch()
