import requests
from bs4 import BeautifulSoup

url="https://www.hanbit.co.kr/store/books/full_book_list.html"
r=requests.get(url)

soup=BeautifulSoup(r.text, "html.parser")

data=soup.find_all("td",attrs={"class":"left"})
for i in data:
    if i.a:
        print(i.a.get_text())
