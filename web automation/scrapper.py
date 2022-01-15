import requests
from bs4 import BeautifulSoup
url = 'https://www.thenetnaija.co/music'
html = requests.get(url)
bsObj = BeautifulSoup(html.content)
h2 = bsObj.find_next_sibling('h2')
print(h2)
#for mlist in h2:
#    print(mlist.get_text())
#print(bsObj.getText())
#print(h2)
