import requests
from bs4 import BeautifulSoup

url="https://www.melon.com/chart/index.htm"
headers = {"User-Agent":""}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

#  멜론 1등부터 100등까지

ranks = soup.tbody.find_all("tr")
for i,rank in enumerate(ranks):
    rank_num = rank.find("span",{"class":"rank01"}).span.a.get_text()
    print("{}위 : {}",format(rank))


