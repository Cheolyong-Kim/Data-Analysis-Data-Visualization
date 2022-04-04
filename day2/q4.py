import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/sise_rise.naver"
r=requests.get(url)

soup=BeautifulSoup(r.text, "html.parser")
data1=soup.select("a.tltle")
data2=soup.select("td.number")
l1=[]
l2=[]
l3=[]
l4=[]

for i in data1:
    l1.append(i.get_text()) #종목명만 빼내서 l1에

for i in data2:
    l2.append(i.get_text().strip()) #td.number에 있는 값들을 모두 l2에

for i in range(len(l2)):
    if i%10==0:
        l3.append(l2[i]) #첫번째 값(현재가)을 모두 l3에
    if i%10==8:
        l4.append(l2[i]) #9번째 값(PER)을 모두 l4에

for i in range(len(l1)):
    print(f"종목명: {l1[i]} | 현재가: {l3[i]} | PER: {l4[i]}")