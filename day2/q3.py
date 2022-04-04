import requests
from bs4 import BeautifulSoup

url="https://movie.naver.com/movie/point/af/list.naver"
r=requests.get(url)

soup=BeautifulSoup(r.text, "html.parser")
data=soup.select("td.title")

for i in data:
    print(i.br.next_sibling.strip())
