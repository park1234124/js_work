from nturl2path import url2pathname
import requests
from bs4 import BeautifulSoup

url = "https://shoppinghow.kakao.com/siso/p/bestRank/"
res = requests.get(url)
res.raise_for_status

soup=BeautifulSoup(res.text, "lxml")

total_num = 0
shopping = soup.find_all("tr")

for shopping in shopping:
    try:
        s_title= shopping.find("li",{"class":"title"}).a.get_text()
        s_num = shopping.find("div",{"class":"rating_type"}).strong.get_text()
        total_num += float(c_num)   #string -> float
        count += 1
        print("제목 : {},평점: {}".format(c_title,c_num))
    except:
        pass
    print(" : ",total_num,2))
    print(" : ",total_num/count,2))
    