import requests
from bs4 import BeautifulSoup

url="https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%8C%EC%9A%B0%EC%A0%88"
r=requests.get(url)

soup=BeautifulSoup(r.text, "html.parser")
data=soup.select("a.api_txt_lines total_tit _cross_trigger")

for i in data:
    t=i.get_text()
    print(t)
