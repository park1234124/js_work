import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find("a",{""})


total_rank = soup.find("ol",{"id":"realTimeRankFavorite"})
ranks = total_rank.find_all("li");
for i,rank in enumerate(ranks):
print(i+1,"위 : ",ranks[i].a.get_text())