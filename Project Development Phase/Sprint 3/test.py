import requests
from bs4 import BeautifulSoup

# def get_weather(place):
url='https://www.google.com/search?&q=calories in '+'dal makhani'
req=requests.get(url).text
print(req)
scrap=Beautifulsoup(req,'html.parser')
tmp = scrap.find("div", class_= "BNeawe iBp4i AP7Wnd").text
print(tmp)
