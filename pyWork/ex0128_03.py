import requests
from bs4 import BeautifulSoup

url="https://www.naver.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# title 태그를 가지고옴
# print(soup.title)
print(soup.title)
# title태그 글자를 가지고 옴.
print(soup.title.get_text())

print(soup.a)