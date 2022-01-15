from email import parser
import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=python"

content = requests.get(url)

contentBsObj = BeautifulSoup(content.text,'html.parser')

span_data = contentBsObj.find_all('div', {'id':'metadata'})
print(len(span_data))
print(span_data)

#for i in span_data:
#    print(i)

#print(content.text)

#contentBsObj.get_text()
#views = contentBsObj.find("span", {"class": "style-scope ytd-video-meta-block"} )

#for v in views:
#   print(v.get_text())
#print(views)