import requests
from bs4 import BeautifulSoup

url="http://www.hanbit.co.kr/store/books/full_book_list.html"
r=requests.get(url)

soup=BeautifulSoup(r.text, "html.parser")

data1=soup.find("li") #li태그는 순서가 정해져있음.
print(data1)
print(data1.get_text())
print('')

data2=data1.next_sibling.next_sibling #next_sibling으로 다음 순서의 데이터를 가져올 수 있음
print(data2)
print(data2.get_text())
print('')

data3=data2.next_sibling.next_sibling
print(data3)
print(data3.get_text())
print('')

data_all=soup.find_all("li")

a=soup.find('a', text="한빛미디어")
print(a)