import requests
from bs4 import BeautifulSoup

def f(n,x): #입력값 x만큼 next_sibling하여 원하는 정보만 출력하는 함수
    for i in range(x):
        n=n.next_sibling
    return n.text

url = 'https://finance.naver.com/sise/sise_rise.naver'
r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser")
data=soup.select("td")

for i in data:
    if i.a:
        print(f"종목명:{i.a.text},현재가:{f(i,2)},PER{f(i,18)}")