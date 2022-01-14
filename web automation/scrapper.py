import requests
from bs4 import BeautifulSoup
url = 'https://www.thenetnaija.co/music'
html = requests.get(url)
bsObj = BeautifulSoup(html.content,)
h2 = bsObj.find('h2')
print(bsObj.getText())
print(h2.get_text())
