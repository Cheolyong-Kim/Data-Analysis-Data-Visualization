import requests
from bs4 import BeautifulSoup

url="https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98"
r=requests.get(url)

soup=BeautifulSoup(r.text, "html.parser")
data=soup.select("a.news_tit")

for i in data:
    print(i.get_text())