import requests
from bs4 import BeautifulSoup

url="https://movie.naver.com/movie/point/af/list.naver"
r=requests.get(url)

soup=BeautifulSoup(r.text, "html.parser")

data=soup.find_all("td", attrs={"class": "title"})
for i in data:
    print(i.a.get_text())

for i in soup.select('td[class=title]'): #위와 동일한 동작. select를 이용
    print(i.a.text.strip())