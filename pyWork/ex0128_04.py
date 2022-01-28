import requests
from bs4 import BeautifulSoup

url="https://www.naver.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.find("a",{"class":"btn_logout"}))
a1 = soup.find("div",{"id":"account"})
# print(soup.find("span"),{"class":"blind"}).get_text())
print(a1.next_sibling)
