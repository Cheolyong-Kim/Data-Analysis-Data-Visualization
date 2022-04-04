import requests
from bs4 import BeautifulSoup

def f(i,x):
    for n in range(x):
        i=i.next_sibling
    return i.text.strip()

url="https://finance.naver.com/sise/sise_rise.naver?sosok=1"
r=requests.get(url)

soup=BeautifulSoup(r.text, "html.parser")
data=soup.select("td")

for i in data:
    if i.a:
        print(f"종목명: {i.a.text}  |  현재가: {f(i,2)}  |  전일비: {f(i,4)}  |  등락률: {f(i,6)}")
