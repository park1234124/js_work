import requests

# 정보요청
res = requests.get(url)

print("응답 코드 : ",res.status_code)