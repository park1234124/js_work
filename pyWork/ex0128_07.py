import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=748105&weekday=sun"
res= requests.get(url)
res.raise_for_status

soup=BeautifulSoup(res.text, "lxml")

total_num = 0
cartoons = soup.find_all("tr")

for cartoon in cartoons:
    try:
        c_title= cartoon.find("td",{"class":"title"}).a.get_text()
        c_num = cartoon.find("div",{"class":"rating_type"}).strong.get_text()
        total_num += float(c_num)   #string -> float
        count += 1
        print("제목 : {},평점: {}".format(c_title,c_num))
    except:
        pass
    print("전체 점수 : ",total_num,2))
    print("평균 점수 : ",total_num/count,2))