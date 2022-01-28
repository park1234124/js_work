import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=748105&weekday=sun"
res= requests.get(url)
res.raise_for_status

soup=BeautifulSoup(res.text, "lxml")

    
cartoons = soup.find_all("tr")

for cartoon in cartoons[2::]:
    title= cartoon.find("td",{"class":"title"}).a.get_text()
    num = cartoon.find("div",{"class":"rating_type"}).strong.get_text()
    print(title, num)