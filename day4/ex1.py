import requests
from bs4 import BeautifulSoup

r=requests.get("https://movie.naver.com/movie/point/af/list.naver")
s=BeautifulSoup(r.text, 'html.parser')
s.previous_sibling
print(s.a.next_sibling)
